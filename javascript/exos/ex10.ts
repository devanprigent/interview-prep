/*
On reçoit une liste d’éléments. On veut savoir combien de fois chaque élément apparaît.
*/

function ocurrences(elements: string[]) {
  const occ = new Map();
  elements.forEach((el) => {
    const curr = occ.get(el) ?? 0;
    occ.set(el, curr + 1);
  });
  return occ;
}

/*
SOLUTION

La complexité temporelle est O(n).

La complexité spatiale est O(n).
*/
