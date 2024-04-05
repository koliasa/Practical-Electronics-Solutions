<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Solitaire</title>
  <style>
    body {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      background-color: #e6e6e6;
    }
    .card {
      width: 60px;
      height: 80px;
      border: 1px solid black;
      border-radius: 5px;
      display: inline-block;
      margin: 5px;
      text-align: center;
      line-height: 80px;
      cursor: pointer;
      background-color: white;
    }
  </style>
</head>
<body>
  <div id="game">
    <!-- Game cards will be added dynamically using JavaScript -->
  </div>

  <script>
    const suits = ['♠', '♥', '♦', '♣'];
    const values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
    const gameContainer = document.getElementById('game');

    // Function to generate deck of cards
    function generateDeck() {
      let deck = [];
      for (let suit of suits) {
        for (let value of values) {
          deck.push({ suit, value });
        }
      }
      return deck;
    }

    // Function to shuffle deck of cards
    function shuffleDeck(deck) {
      for (let i = deck.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [deck[i], deck[j]] = [deck[j], deck[i]];
      }
    }

    // Initialize game
    function initGame() {
      let deck = generateDeck();
      shuffleDeck(deck);
      renderCards(deck);
    }

    // Function to render cards on screen
    function renderCards(deck) {
      gameContainer.innerHTML = '';
      deck.forEach(card => {
        let cardElement = document.createElement('div');
        cardElement.className = 'card';
        cardElement.textContent = card.value + card.suit;
        gameContainer.appendChild(cardElement);
      });
    }

    // Call initGame to start the game
    initGame();
  </script>
</body>
</html>
