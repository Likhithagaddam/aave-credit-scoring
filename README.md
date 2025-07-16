Aave V2 Credit Scoring Project

#1. Overview
This project calculates a credit score for each wallet based on how it interacted with the Aave V2 DeFi protocol. The scores range from 0 (risky) to 1000 (trustworthy). The data includes actions like deposit, borrow, repay, and liquidation.


#2. Project Structure
Main files and folders:
- data/: Contains the input JSON file
- src/: Python code for feature extraction and scoring
- output/: Generated scores and plots
- README.md: Project summary
- analysis.md: Wallet behavior analysis


#3. Features Used
Each wallet’s score is based on:
- Total deposit amount
- Total borrow and repay amounts
- Repay-to-borrow ratio
- Liquidation count
- Redemption count
- Activity duration in days

  
#4. Scoring Rules
Rules were assigned simple weights to evaluate responsible behavior.
- More deposits, repayments, and long-term activity = higher score
- Frequent liquidations or no repayment = lower score
- Final score is capped at 1000

