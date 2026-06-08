import React from "react";
import { createRoot } from "react-dom/client";

type Ingredient = {
  name: string;
  amount: number;
  measurement: string;
};

type RecipeType = {
  name: string;
  ingredients: Ingredient[];
  steps: string[];
};

const data: RecipeType[] = [
  {
    name: "Baked Salmon",
    ingredients: [
      { name: "Salmon", amount: 1, measurement: "lb" },
      { name: "Pine Nuts", amount: 1, measurement: "cup" },
      { name: "Butter Lettuce", amount: 2, measurement: "cups" },
      { name: "Yellow Squash", amount: 1, measurement: "med" },
      { name: "Olive Oil", amount: 0.5, measurement: "cup" },
      { name: "Garlic", amount: 3, measurement: "cloves" }
    ],
    steps: [
      "Preheat the oven to 350 degrees.",
      "Spread the olive oil around a glass baking dish.",
      "Add the salmon, garlic, and pine nuts to the dish.",
      "Bake for 15 minutes.",
      "Add the yellow squash and put back in the oven for 30 mins.",
      "Remove from oven and let cool for 15 minutes. Add the lettuce and serve."
    ]
  },
  {
    name: "Fish Tacos",
    ingredients: [
      { name: "Whitefish", amount: 1, measurement: "lb" },
      { name: "Cheese", amount: 1, measurement: "cup" },
      { name: "Iceberg Lettuce", amount: 2, measurement: "cups" },
      { name: "Tomatoes", amount: 2, measurement: "large" },
      { name: "Tortillas", amount: 3, measurement: "med" }
    ],
    steps: [
      "Cook the fish on the grill until hot.",
      "Place the fish on the 3 tortillas.",
      "Top them with lettuce, tomatoes, and cheese."
    ]
  }
];

type RecipeProps = RecipeType;
const Recipe: React.FC<RecipeProps> = ({ name, ingredients, steps }) => (
  <section className="bg-white p-6 rounded-lg shadow-md m-4">
    <h1 className="text-2xl font-bold text-blue-600">{name}</h1>
    <h2 className="text-lg font-semibold mt-4">Ingredients:</h2>
    <ul className="list-disc list-inside text-gray-700">
      {ingredients.map((ingredient, i) => (
        <li key={i}>
          {ingredient.amount} {ingredient.measurement} {ingredient.name}
        </li>
      ))}
    </ul>
    <h2 className="text-lg font-semibold mt-4">Cooking Instructions:</h2>
    <ol className="list-decimal list-inside text-gray-700">
      {steps.map((step, i) => (
        <li key={i}>{step}</li>
      ))}
    </ol>
  </section>
);

type MenuProps = {
  title: string;
  recipes: RecipeType[];
};

const Menu: React.FC<MenuProps> = ({ title, recipes }) => (
  <div className="max-w-3xl mx-auto p-4 ml-[30px]">
    <header className="text-center mb-6">
      <h1 className="text-3xl font-bold text-gray-800">{title}</h1>
    </header>
    <div className="space-y-6">
      {recipes.map((recipe, i) => (
        <Recipe key={i} {...recipe} />
      ))}
    </div>
  </div>
);

const App: React.FC = () => (
  <div className="bg-gray-100 min-h-screen flex items-center justify-center">
      <Menu title="Delicious Recipes" recipes={data} />
  </div>
);
export default App;

const container = document.getElementById("root") as HTMLElement;
const root = createRoot(container);
root.render(<App />);
