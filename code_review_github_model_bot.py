import os
import sys
import requests
import json
from openai import OpenAI

def read_diff_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Diff file not found at {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading diff file: {str(e)}")
        sys.exit(1)

def main():
    # Get command line arguments
    diff_file_path = sys.argv[1]
    pr_number = sys.argv[2]
    repository = sys.argv[3]

    # Read the diff content from file
    diff_content = read_diff_file(diff_file_path)
    
    client = OpenAI(
        base_url="https://models.github.ai/inference",
        api_key=os.environ["AI_MODEL_PAT_TOKEN"],
    )


    # Construct the messages for GPT-4
    messages = [
        {
            "role": "system",
            "content": "You are an expert software engineer conducting a thorough code review."
        },
        {
            "role": "user",
            "content": f"""Please analyze the following code diff and provide detailed, constructive feedback.

Focus your analysis on:
1. Code quality and best practices
2. Potential bugs or security issues
3. Performance considerations
4. Maintainability and readability
5. Suggestions for improvements with specific examples

Here's the code diff to review:

{diff_content}"""
        }
    ]

    try:
        # Call OpenAI API
        response = client.chat.completions.create(
            model="openai/gpt-4o",
            messages=messages,
            temperature=0.7,
            max_tokens=4096
        )

        # Extract the review comment
        review_comment = response.choices[0].message.content

        print("Review comment generated:")
        print(review_comment)
        print("Posting review comment to GitHub PR...")

        # Post comment to GitHub PR
        github_token = os.environ.get('GITHUB_TOKEN')
        if not github_token:
            raise ValueError("GITHUB_TOKEN environment variable is not set")

        api_url = f"https://api.github.com/repos/{repository}/issues/{pr_number}/comments"
        
        headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        data = {
            "body": review_comment
        }

        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()

        print("Code review comment posted successfully!")

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
