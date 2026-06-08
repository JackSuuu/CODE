import java.util.ArrayList;
import java.util.List;

// Read the article and trying to spot the difference
// Make comparsion here
// So, basically the idea of refactoring is that hide the unnecessary part of the code
// And male the code more readable overall, therefore, each uncessary loop can be elminiated
// Additionally, we can use extrat method to replace some duplicate computation by adding inner method
// Here is the refine versio of the code in total

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

    public int getTotalGoalsAgainst() {
        return games.stream().mapToInt(game -> game.getGoalsAgainst()).sum();
    }

    public int getTotalShotsOnGoalAgainst() {
        return games.stream().mapToInt(game -> game.getShotsOnGoalAgainst()).sum();
    }

    public double getTotalMinutesPlayed() {
        return games.stream().mapToDouble(game -> game.getMinutesPlayed()).sum();
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
            int totalGoalsAgainst = season.getTotalGoalsAgainst();
            double totalMinutesPlayed = season.getTotalMinutesPlayed();

            // Goal 1
            return (totalGoalsAgainst / totalMinutesPlayed) * 60;
        }
    }

    public double getSavePercentage() {

        if (season.getGames().isEmpty()) {
            return 0.0;
        }
        else {
            int totalGoalsAgainst = season.getTotalGoalsAgainst();
            int totalSogAgainst = season.getTotalShotsOnGoalAgainst();

            // Goal 2
            return ((double) totalSogAgainst - totalGoalsAgainst) / totalSogAgainst;
        }
    }
}
