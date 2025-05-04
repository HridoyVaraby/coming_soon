import os
import random
from datetime import datetime, timedelta

def generate_commits():
    # Set date range
    start_date = datetime(2024, 4, 3)
    end_date = datetime(2024, 11, 28)
    delta = end_date - start_date
    
    # Create markdown file if not exists
    if not os.path.exists('commits.md'):
        with open('commits.md', 'w') as f:
            f.write('# Commit History\n\n')
    
    # Generate daily commits
    for i in range(delta.days + 1):
        current_date = start_date + timedelta(days=i)
        date_str = current_date.strftime('%Y-%m-%d')
        
        # Add one line to markdown file
        with open('commits.md', 'a') as f:
            f.write(f'Commit on {date_str}\n')
        
        # Git commands with backdating
        os.system(f'git add commits.md')
        os.system(f'git commit --date="{date_str} 12:00:00" -m "Daily commit for {date_str}"')
    
    # Generate random additional commits (5-8)
    num_extra = random.randint(5, 8)
    for _ in range(num_extra):
        random_day = random.randint(0, delta.days)
        current_date = start_date + timedelta(days=random_day)
        date_str = current_date.strftime('%Y-%m-%d')
        
        with open('commits.md', 'a') as f:
            f.write(f'Extra commit on {date_str}\n')
        
        os.system(f'git add commits.md')
        os.system(f'git commit --date="{date_str} 12:00:00" -m "Extra commit for {date_str}"')

if __name__ == '__main__':
    generate_commits()