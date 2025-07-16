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

  
#4. Method Chosen

Used a rule-based scoring approach for transparency and interpretability. Features were extracted from user transaction history such as total deposit, borrow, repay amounts, liquidation count, and wallet activity duration. Each wallet was scored based on positive behaviors (like repaying loans and avoiding liquidation) and penalized for risky behaviors (such as frequent liquidations or low repay ratios).

#5. Processing Flow

The project follows this step-by-step pipeline:

1. Load JSON data containing raw transaction history.

2. Parse transactions by wallet address and categorize actions (deposit, borrow, repay, redeem, liquidation).
   
3. Calculate features like:
   - Total deposit, borrow, repay, and redeem amounts
   - Repay-to-borrow ratio
   - Number of liquidation events
   - Active duration (time between first and last transaction)

4. Assign weighted scores to each wallet based on feature values.

5. Normalize the final score to a scale of 0 to 1000.

6. Export results as a CSV file and create visual analysis (e.g., score distribution chart).



