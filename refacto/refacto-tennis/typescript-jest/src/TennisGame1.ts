import { TennisGame } from "./TennisGame";

export class TennisGame1 implements TennisGame {
  private m_score1: number = 0;
  private m_score2: number = 0;
  private player1Name: string;
  private player2Name: string;

  private matchingScore = ["Love", "Fifteen", "Thirty", "Forty"];

  constructor(player1Name: string, player2Name: string) {
    this.player1Name = player1Name;
    this.player2Name = player2Name;
  }

  wonPoint(playerName: string): void {
    if (playerName === this.player1Name) this.m_score1 += 1;
    else if (playerName === this.player2Name) this.m_score2 += 1;
  }

  getEqualScore(score: number): string {
    if (score < 3) {
      return this.matchingScore[score] + "-All";
    }
    return "Deuce";
  }

  getAdvantageOrWin(score1: number, score2: number) {
    const minusResult: number = score1 - score2;
    if (minusResult === 1) return "Advantage player1";
    else if (minusResult === -1) return "Advantage player2";
    else if (minusResult >= 2) return "Win for player1";
    else return "Win for player2";
  }

  getScore(): string {
    if (this.m_score1 === this.m_score2) {
      return this.getEqualScore(this.m_score1);
    } else if (this.m_score1 >= 4 || this.m_score2 >= 4) {
      return this.getAdvantageOrWin(this.m_score1, this.m_score2);
    }
    return (
      this.matchingScore[this.m_score1] +
      "-" +
      this.matchingScore[this.m_score2]
    );
  }
}
