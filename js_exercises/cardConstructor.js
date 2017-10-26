class Deck
{
    //private opt: DeckOptions;

    cards : Card[];

    constructor (card: Object = {})
    {
        this.card = {
            extend: card['extend'] || [],
            suits: card['suits'] || ['spades', 'hearts', 'diamonds', 'clubs'],
            ranks: card['ranks'] || ['ace', 'king', 'queen', 'jack', '10', '9', '8', '7', '6', '5', '4', '3', '2'],
        };

        this.shuffle();
    }
}
