import os
import random
from datetime import datetime, timedelta

def generate_commits():
    # Set date range
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    delta = end_date - start_date
    
    # Create markdown file if not exists
    if not os.path.exists('commits.md'):
        with open('commits.md', 'w') as f:
            f.write('# Commit History\n\n')
    
    # Select 15 random days
    selected_days = random.sample(range(delta.days + 1), 15)
    
    # Generate 7 commits for each selected day
    for day in selected_days:
        current_date = start_date + timedelta(days=day)
        date_str = current_date.strftime('%Y-%m-%d')
        
        for i in range(7):  # 7 commits per day
            # Random time between 9:00 and 17:00
            hour = random.randint(9, 16)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            time_str = f"{hour:02d}:{minute:02d}:{second:02d}"
            
            # Add commit to markdown file
            with open('commits.md', 'a') as f:
                f.write(f'Commit on {date_str} at {time_str}\n')
            
            # Git command with backdating
            os.system(f'git add commits.md')
            os.system(f'git commit --date="{date_str} {time_str}" -m "Commit for {date_str} at {time_str}"')

if __name__ == '__main__':
    generate_commits()