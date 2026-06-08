package old;
import java.util.ArrayList;
import java.util.List;

// The goal of this application
// 1. Goals Against Average(GAA) - 60 * (GA / time_playerd)
// 2. Save Percentage(SV%) - (SOG - Goals) / SOG

// Main class - Game
public class Game {

    private final double minutesPlayed;
    private final int goalsAgainst;
    private final int shotsOnGoalAgainst;

    public Game(int goalsAgainst, int shotsOnGoalAgainst, double minutesPlayed) {
        this.goalsAgainst = goalsAgainst;
        this.shotsOnGoalAgainst = shotsOnGoalAgainst;
        this.minutesPlayed = minutesPlayed;
    }

    public int getGoalsAgainst() {
        return goalsAgainst;
    }

    public int getShotsOnGoalAgainst() {
        return shotsOnGoalAgainst;
    }

    public double getMinutesPlayed() {
        return minutesPlayed;
    }
}

class Season {

    private final List<Game> games;

    public Season(List<Game> games) {
        this.games = new ArrayList<>(games);
    }

    public Season() {
        this.games = new ArrayList<>();
    }

    public void addGame(Game game) {
        games.add(game);
    }

    public void removeGame(Game game) {
        games.remove(game);
    }

    public List<Game> getGames() {
        return games;
    }

    public GoalieStatistics getGoalieStatistics() {
        return new GoalieStatistics(this);
    }
}

class GoalieStatistics {

    private final Season season;

    public GoalieStatistics(Season season) {
        this.season = season;
    }

    public double getGoalsAgainstAverage() {

        if (season.getGames().isEmpty()) {
            return 0.0;
        }
        else {
            List<Game> games = season.getGames();
            
            // the loop can be split up into two
            // for (Game game: games) {
            //     tga += game.getGoalsAgainst();
            //     mins += game.getMinutesPlayed();
            // }
            int tga = getTotalGoalsAgainst(games);

            double mins = 0;
            for (Game game : games) {
                mins += game.getMinutesPlayed();
            }

            return (tga / mins) * 60;
        }
    }

    // To refactor further, we create a private method for tga
    private int getTotalGoalsAgainst(List<Game> games) {
        int g = 0;

        for (Game game : games) {
            g += game.getGoalsAgainst();
        }
        return g;
    }

    public double getSavePercentage() {

        if (season.getGames().isEmpty()) {
            return 0.0;
        }
        else {
            List<Game> games = season.getGames();
            
            // It can apply the same here
            int g = getTotalGoalsAgainst(games);

            int tsoga = 0;
            for (Game game: games) {
                tsoga += game.getShotsOnGoalAgainst();
            }
            
            return ((double) tsoga - g) / tsoga;
        }
    }
}