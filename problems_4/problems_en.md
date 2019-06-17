# Tree as a Service
Carlos is hoping to strike it rich with his new consulting firm, Carlos Structures Industries (CSI). With a solid mission statement and a can-do attitude, he's sure to succeed in the wide world of bespoke data structures.  
  
"Our vision is to synergistically leverage our core competencies to deliver competitive market solutions that assertively meet our clients' needs."  
  
His first client, the well-known translation firm Treehouse, is looking to update their logo. Treehouse wants their logo to be a rooted tree with N nodes numbered 1 through N. They have a rough idea of what the tree should look like, but they want Carlos to finish fleshing it out. In particular, they have M requirements, the ith of which states that the lowest common ancestor of nodes Xi and Yi must be node Zi.  
  
Carlos's goal is to find any valid tree consistent with all of these requirements if possible, or to determine that no such tree exists.  
  
## Input
Input begins with an integer T, the number of tree designs. For each design, there is first a line containing the space-separated integers N and M. Then M lines follow, the ith of which contains the space-separated integers Xi, Yi, and Zi.  

## Output
For the ith design, print a line containing "Case #i: " followed by a description of a valid rooted tree if possible, or the string "Impossible" if no valid tree exists. A tree description is N space-separated integers, the jth of which is node j's parent (or 0 if node j is the root).  

## Constraints
1 ≤ T ≤ 100   
2 ≤ N ≤ 60   
1 ≤ M ≤ 120   
1 ≤ Xi, Yi, Zi ≤ N   
Xi ≠ Yi  

## Explanation of Sample
In the first case, the LCA of nodes 1 and 2 in the chosen tree is 3, as required. This is the only valid output for this case.  

In the third case, "2 3 0 3" would also be accepted, while no other outputs would be.  

In the fifth and sixth cases, multiple possible outputs would be accepted.  
