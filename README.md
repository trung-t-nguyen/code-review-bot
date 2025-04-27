# Code Review bot

An automated code review tool that leverages AWS Bedrock Claude to provide intelligent code review comments on GitHub pull requests.

## Features

- Automated code review using AWS Bedrock Claude AI
- GitHub Pull Request integration
- Detailed feedback on:
  - Code quality and best practices
  - Potential bugs and security issues
  - Performance considerations
  - Maintainability and readability
  - Specific suggestions for improvements

## Prerequisites

- Python 3.x
- AWS account with Bedrock access
- GitHub repository access
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/code-review-bot.git
cd code-review-bot
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Set up AWS credentials:
```bash
export AWS_ACCESS_KEY_ID='your-access-key'
export AWS_SECRET_ACCESS_KEY='your-secret-key'
export AWS_DEFAULT_REGION='us-east-1'
```

2. Set up GitHub token:
```bash
export GITHUB_TOKEN='your-github-token'
```

## Usage

Run the code review script:
```bash
python code_review_script/code_review_bot.py "/path/to/diff.txt" "PR_NUMBER" "REPOSITORY_NAME"
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

[Add your license information here]

## Authors

[Add author information here]