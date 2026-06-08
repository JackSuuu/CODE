public class OOP_A1_Test_2 {
    private static final String ROCK_INPUT = "rock";
    private static final String PAPER_INPUT = "paper";
    private static final String SCISSORS_INPUT = "scissors";

    private static final int INVALID = -1;
    private static final int ROCK = 1;
    private static final int PAPER = 2;
    private static final int SCISSORS = 3;

    private static int getChoice_case(String processdINPUT) {
        switch (processdINPUT) {
            case ROCK_INPUT: return ROCK;
            case  PAPER_INPUT: return PAPER;
            case SCISSORS_INPUT: return SCISSORS;
            default: return INVALID;
        }
    }

    private static int getChoiceIfElse(String processedInput)
    {
        if (processedInput.equals(ROCK_INPUT))
        {
            return ROCK;
        } else
        {
            if (processedInput.equals(PAPER_INPUT))
            {
                return PAPER;
            } else
            {
                if (processedInput.equals(SCISSORS_INPUT))
                {
                    return SCISSORS;
                }
            }
        }
        return INVALID;
    }

    public static boolean isValidChoice(int playerChoice) {
        if (playerChoice >= ROCK && playerChoice <= SCISSORS)
            return true;
        else
            return false;
    }

    public static void main(String[] args) {
        System.out.println(getChoice_case("rock"));
        System.out.println(getChoiceIfElse("paper"));
    }
}
