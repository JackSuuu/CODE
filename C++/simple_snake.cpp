#include <SFML/Graphics.hpp>
#include <iostream>

// Define the size of the grid
const int gridSize = 20;
const int gridWidth = 20;
const int gridHeight = 10;

class SnakeGame {
    public:
        SnakeGame();
        void run();

    private:
        void handleInput();
        void update();
        void render();

        sf::RenderWindow window;
        sf::Clock clock;

        sf::Vector2i snakeDirection;
        std::vector<sf::Vector2i> snake;
        sf::Vector2i fruit;

        int score;
};

SnakeGame::SnakeGame() : window(sf::VideoMode(gridWidth * gridSize, gridHeight * gridSize), "Snake Game") {
    window.setFramerateLimit(10); // Limit the frame rate to make the game playable

    snakeDirection = sf::Vector2i(1, 0); // Initial direction (right)
    snake.push_back(sf::Vector2i(5, 5)); // Initial position of the snake
    fruit = sf::Vector2i(10, 5);         // Initial position of the fruit
    score = 0;
}

void SnakeGame::handleInput() {
    sf::Event event;
    while (window.pollEvent(event)) {
        if (event.type == sf::Event::Closed)
            window.close();
        else if (event.type == sf::Event::KeyPressed) {
            if (event.key.code == sf::Keyboard::Up && snakeDirection.y == 0)
                snakeDirection = sf::Vector2i(0, -1);
            else if (event.key.code == sf::Keyboard::Down && snakeDirection.y == 0)
                snakeDirection = sf::Vector2i(0, 1);
            else if (event.key.code == sf::Keyboard::Left && snakeDirection.x == 0)
                snakeDirection = sf::Vector2i(-1, 0);
            else if (event.key.code == sf::Keyboard::Right && snakeDirection.x == 0)
                snakeDirection = sf::Vector2i(1, 0);
        }
    }
}

void SnakeGame::update() {
    if (clock.getElapsedTime().asSeconds() >= 0.1)
    {
        // Move the snake
        sf::Vector2i newHead = snake.front() + snakeDirection;
        snake.insert(snake.begin(), newHead);

        // Check for collision with the fruit
        if (newHead == fruit)
        {
            score++;
            // Generate a new fruit at a random position
            fruit.x = rand() % gridWidth;
            fruit.y = rand() % gridHeight;
        }
        else
        {
            // Remove the tail if the snake did not eat a fruit
            snake.pop_back();
        }

        // Check for collision with the walls or itself
        if (newHead.x < 0 || newHead.x >= gridWidth || newHead.y < 0 || newHead.y >= gridHeight)
        {
            window.close();
            std::cout << "Game Over! Score: " << score << std::endl;
        }

        for (size_t i = 1; i < snake.size(); ++i)
        {
            if (newHead == snake[i])
            {
                window.close();
                std::cout << "Game Over! Score: " << score << std::endl;
            }
        }

        clock.restart();
    }
}

void SnakeGame::render() {
    window.clear();

    // Draw the snake
    for (const auto &segment : snake)
    {
        sf::RectangleShape rectangle(sf::Vector2f(gridSize - 1, gridSize - 1));
        rectangle.setPosition(segment.x * gridSize, segment.y * gridSize);
        rectangle.setFillColor(sf::Color::Green);
        window.draw(rectangle);
    }

    // Draw the fruit
    sf::RectangleShape fruitRectangle(sf::Vector2f(gridSize - 1, gridSize - 1));
    fruitRectangle.setPosition(fruit.x * gridSize, fruit.y * gridSize);
    fruitRectangle.setFillColor(sf::Color::Red);
    window.draw(fruitRectangle);

    window.display();
}

void SnakeGame::run() {
    while (window.isOpen()){
        handleInput();
        update();
        render();
    }
}

int main() {
    SnakeGame game;
    game.run();

    return 0;
}
