/*
On te donne une liste d’utilisateurs et une liste d’utilisateurs actifs. 

On veut retourner les utilisateurs qui sont actifs.

Une première implémentation parcourt les deux listes avec deux boucles.

**Explique ce que fait le code, donne sa complexité, puis propose une optimisation.
*/

function getActiveUsers(users: string[], activeUsers: string[]) {
  const filteredActiveUsers = [];
  for (let i = 0; i < users.length; i++) {
    for (let j = 0; j < activeUsers.length; j++) {
      if (users[i] === activeUsers[j]) {
        filteredActiveUsers.push(users[i]);
      }
    }
  }
  return filteredActiveUsers;
}

function getActiveUsers2(users: string[], activeUsers: string[]) {
  const filteredUsers = users.filter((user) => activeUsers.includes(user));
  return filteredUsers;
}

/*
Le code parcourt les deux listes pour trouver leur intersection.

La première solution utilise deux boucles explicitement tandis que

la deuxième utilise deux boucles implicitement avec filter et includes.

Dans les deux cas la complexity est O(n*m) où n et m sont les tailles des 

listes.

Une optimisation est d'utiliser un set à la place pour profiter d'un lookup 

constant et obtenir une complexité linéaire.

Le compromis, c'est qu'on utilise O(m) de mémoire supplémentaire pour stocker 

le Set, mais on gagne énormément en temps d'exécution.
*/

function optimizedSolution(users: string[], activeUsers: string[]) {
  const optimizedActiveUsers = new Set(activeUsers);
  return users.filter((user) => optimizedActiveUsers.has(user));
}
