class DeckOfCards
  {



     /* ---------------------------------------------------
        The constructor method: make 52 cards in a deck
  --------------------------------------------------- */
     DeckOfCards( )
     {
        /* =================================================================
           First: create the array
           ================================================================= */
    deckOfCards = new Card[ 52 ];   // Very important !!!
                                            // We must crate the array first !

        /* =================================================================
           Next: initialize all 52 card objects in the newly created array
           ================================================================= */
    var i = 0;

    for (suit = Card.DIAMOND; suit <= Card.SPADE; suit++ )
       for (rank = 1; rank <= 13; rank++ )
     deckOfCards[i++] = new Card(suit, rank);  // Put card in
                                                         // position i
