# Auction

The auction module manages live auction sessions where bidders compete in real-time to purchase items.

## Overview

During a live auction, the auctioneer uses the **Clerk Screen** to control the auction flow, accept bids from multiple channels (floor, phone, online), and record winning bids.

## Key Features

- **Real-time bidding** - Accept bids from floor, phone bidders, and online bidders simultaneously
- **Session management** - Control auction start, pause, and completion
- **Bid tracking** - Record all bids with bidder information and timestamps
- **Item navigation** - Move through lots sequentially or jump to specific items
- **Result recording** - Mark items as sold, passed, or withdrawn

## Documentation

- **[Live Auction Flow](auction-flow.md)** - Understanding the complete auction process
- **[The Clerk Screen](clerk-screen/README.md)** - Detailed guide to the auctioneer's control panel

## Workflow

1. Set up the sale with assigned lot numbers
2. Configure the auction session
3. Start the auction and set status to "live"
4. Process bids item by item
5. Record results for each lot
6. Complete the session when auction ends

For step-by-step instructions on using the clerk screen, see the [Clerk Screen documentation](clerk-screen/README.md).
