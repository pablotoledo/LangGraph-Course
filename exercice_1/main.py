from dotenv import load_dotenv
load_dotenv()

import os

print(str(os.getenv('OPENAI_API_KEY')))

if __name__ == '__main__':
    print('Hello World!')