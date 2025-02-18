import getBudgetObject from './7-getBudgetObject';

export default function getFullBudgetObject(income, gdp, capita) {
  // Obtenir l'objet budget de base
  const budget = getBudgetObject(income, gdp, capita);

  // Étendre l'objet budget avec des méthodes supplémentaires
  const fullBudget = {
    ...budget,
    getIncomeInDollars(income) {
      return `$${income}`;
    },
    getIncomeInEuros(income) {
      return `${income} euros`;
    },
  };

  // Retourner l'objet étendu
  return fullBudget;
}
