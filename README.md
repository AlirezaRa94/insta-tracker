# Insta-tracker

Insta-tracker is a Python project that connects to an Instagram account and retrieves the followers and following of a specified Instagram user. It also displays users you don't follow back and users who don't follow you back.

## Features
- Log in to an Instagram account
- Retrieve followers and following of a target user
- Display users you don't follow back
- Display users who don't follow you back

## Requirements
- Python 3.6 or higher
- An Instagram account

## Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/AlirezaRa94/insta-tracker.git
cd insta-tracker
```

### Step 2: Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies. You can create a virtual environment using the following command:

```bash
python -m venv env
```

### Step 3: Activate the Virtual Environment
On Windows:
```bash
.\env\Scripts\activate
```
On macOS/Linux:
```bash
source env/bin/activate
```

### Step 4: Install the Required Dependencies
Install the dependencies listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```

## Usage
To run the script and retrieve the followers and following of a target Instagram user, follow these steps:

Open the main.py file and replace the following placeholders with your Instagram credentials and the target username:

```python
YOUR_USERNAME = 'YOUR_USERNAME'
YOUR_PASSWORD = 'YOUR_PASSWORD'
TARGET_USERNAME = 'YOUR_TARGET_USERNAME'
```

Run the script:

```bash
python main.py
```

## Example
Here is an example of what the output might look like:

```python
Followers of YOUR_TARGET_USERNAME you don't follow back:
follower1
follower2
follower3
...

Following of YOUR_TARGET_USERNAME they don't follow you back:
followee1
followee2
followee3
...
```

## Notes
- Ensure that your Instagram account credentials are kept secure and not hardcoded in public repositories.
- Be aware of Instagram's rate limits to avoid temporary bans.
- If your Instagram account has two-factor authentication enabled, you will need to handle this within the script. Refer to the instaloader documentation for more details on managing two-factor authentication.
