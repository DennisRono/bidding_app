# Bidding App

## Overview

The Bidding App is a web application built with FastAPI that allows users to participate in online auctions. Users can place bids on items and the highest bid wins when the auction ends.

## Features

- User registration and authentication
- Create and manage auctions
- Place bids on items
- Real-time updates on auction status
- Notifications for bid status and auction results

## Installation

To install and run the Bidding App locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/DennisRono/bidding_app.git
   cd bidding_app
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   uvicorn main:app --reload
   ```

5. Open your browser and navigate to `http://127.0.0.1:8000` to access the application.

## Usage

1. Register a new account or log in with an existing account.
2. Create a new auction by providing item details and starting bid.
3. Browse available auctions and place bids on items of interest.
4. Monitor your bids and receive notifications on auction status.
