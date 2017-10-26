// @flow
const AVAILABLE_SUITS = ['Spade', 'Heart', 'Club', 'Diamond'];
const AVAILABLE_RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];

/**
 * Notes one playing card with suit and rank.
 * @class Card
 */

  constructor(params: { suit: string, rank: string }) {
    if (AVAILABLE_SUITS.indexOf(params.suit) === -1) {
      throw new Error('Unrecognized suit');
    }

    if (AVAILABLE_RANKS.indexOf(params.rank) === -1) {
      throw new Error('Unrecognized rank');
    }

    this._suit = params.suit;
    this._rank = params.rank;
  }

  get suit(): string {
    return this._suit;
  }

  get rank(): string {
    return this._suit.toUpperCase();
  }

  /**
   * Compares current card instance with other card.
   * @param Card otherCard - card to Compare
   * @returns number result -1 when small, 1 when big, 0 when same.
   */
  compare = (otherCard: Card): number => {
    const mySuitIndex = AVAILABLE_SUITS.indexOf(this.suit);
    const myRankIndex = AVAILABLE_RANKS.indexOf(this.rank);
    const otherSuitIndex = AVAILABLE_SUITS.indexOf(otherCard.suit);
    const otherRankIndex = AVAILABLE_SUITS.indexOf(otherCard.rank);

    return (mySuitIndex - otherSuitIndex) || (myRankIndex - otherRankIndex);
  }

  toString = (): string => {
    return `${this._suit} ${this._rank}`;
  }
}

/**
 * Deck of playing cards.
 * @class CardDeck
 */
export class CardDeck {
  cardArray: Array<Card>;

  constructor() {
    this.reset();
  }

  /**
   * Fills card deck with 52 cards.
   */
  reset = () => {
    this.cardArray = [];
    AVAILABLE_SUITS.forEach((suit: string) => {
      AVAILABLE_RANKS.forEach((rank: string) => {
        this.cardArray.push(new Card({ suit, rank }));
      });
    })
  }
