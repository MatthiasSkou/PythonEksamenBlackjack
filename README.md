# Python exam project - BLACKJACK - KEA 2019

Assignment 2 - A console application of the card game: Blackjack

┌───────┐┌───────┐
| J     || A     |
|       ||       |
|   ♦   ||   ♥   |
|       ||       |
|     J ||     A |
└───────┘└───────┘

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
  ```
  1. Start out by downloading the project zip to your local machine https://github.com/MatthiasSkou/PythonEksamenBlackjack.
  2. Extract the zip file.
  3. Open your favorite IDE(ex. Visual Studio Code), hit File --> Open, find the extracted project and open it.
  4. Open the Blackjack.py file.
  5. Hit 'Run' or type 'python Blackjack.py' in your terminal.
  ```

## Functions

This section will describe the different functionalities in the application and how to use them.

### Player

As a player you will have the following options once you start the game:

```
  1. First you need to choose the amount you want to bet from the following options: 10, 20, 30, 40 or 50
    1.1 You can not exceed your current balance
    1.2 You can not enter any other amount than the ones listed above
  2. You are dealt two cards and one of the following two scenarios will occur:
    2.1 You hit blackjack(21 value on initial hand)
      2.1.1 Your turn automatically ends and the dealer starts their turn
    2.2 Your total value is less than 21 and you need to either hit or stand
      2.2.1 If you choose to hit - a card will be added to your hand
      2.2.2 If you choose to stand - your turn will end and dealers turn will begin
  3. Once dealers turn is done, the outcome of the game will be decided. After this, balance will be updated accordingly and        you can choose if you want to play another round.
```

### Dealer

As a dealer you will have the following options once you start the game:

```
  1. Players turn will be played automatically.
  2. Dealer will automatically hit if below 17. 
  3. Game outcome is decided, balances are updated and you may choose to continue playing.
```

## Rules

For an extensive list of official Blackjack rules, please see: * [Blackjack Rules](https://en.wikipedia.org/wiki/Blackjack)

### Missing rules

```
  1. Splitting
  2. Double-down
  3. Safety (15 %)
  4. Super 7
  5. Hard/soft 17
```

## Unit-testing

In order to run the unit-tests for this application, follow the instructions below:

```
  1. Open the test_unit.py file and hit run or type the following command in the terminal: 'python test_unit.py'
  2. If you want to skip the console prints throughout the unit-tests, you can add '-b' to the terminal command.
```

## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - The IDE used for developing this project

## Authors

* **Matthias Skou** - [MatthiasSkou](https://github.com/MatthiasSkou)
