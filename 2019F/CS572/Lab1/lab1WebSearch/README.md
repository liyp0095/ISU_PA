<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [CS572 Lab1](#cs572-lab1)
  - [Platform](#platform)
  - [How to run](#how-to-run)
  - [Runtime result](#runtime-result)
  - [result](#result)
  - [discussion](#discussion)
    - [Task 2a)](#task-2a)
    - [Task 2c)](#task-2c)
  - [Future work](#future-work)
<!-- TOC END -->



# CS572 Lab1

## Platform

java 8 + elementory OS

## How to run

```sh
sh runSearch.sh
```

## Runtime result

*we have runtime result in result_runtime.txt*

```sh
============== Task 1 ================
intranet 1 :
 + Reverse path : page50.html page99.html page29.html page18.html page1.html
 + Path Length : 4
 + Visited 91 nodes, starting @ intranet1/page1.html, using: breadth search.

 + Reverse path : page50.html page83.html page2.html page79.html page87.html page93.html page68.html page30.html page84.html page42.html page25.html page78.html page39.html page60.html page23.html page1.html
 + Path Length : 15
 + Visited 58 nodes, starting @ intranet1/page1.html, using: depth search.

intranet 5 :
 + Reverse path : page62.html page72.html page95.html page96.html page87.html page89.html page99.html page40.html page1.html
 + Path Length : 8
 + Visited 88 nodes, starting @ intranet5/page1.html, using: breadth search.

 + Reverse path : page62.html page72.html page95.html page7.html page48.html page68.html page97.html page5.html page99.html page40.html page1.html
 + Path Length : 10
 + Visited 42 nodes, starting @ intranet5/page1.html, using: depth search.

intranet 7 :
 + Reverse path : page86.html page61.html page62.html page57.html page71.html page48.html page1.html
 + Path Length : 6
 + Visited 56 nodes, starting @ intranet7/page1.html, using: breadth search.

 + Reverse path : page86.html page78.html page11.html page60.html page39.html page90.html page57.html page71.html page48.html page1.html
 + Path Length : 9
 + Visited 12 nodes, starting @ intranet7/page1.html, using: depth search.

============== Task 2a ===============
intranet 1 :
 + Reverse path : page50.html page83.html page2.html page79.html page56.html page95.html page18.html page1.html
 + Path Length : 7
 + Visited 26 nodes, starting @ intranet1/page1.html, using: best search.

intranet 5 :
 + Reverse path : page62.html page72.html page95.html page96.html page87.html page89.html page99.html page40.html page1.html
 + Path Length : 8
 + Visited 26 nodes, starting @ intranet5/page1.html, using: best search.

intranet 7 :
 + Reverse path : page86.html page61.html page73.html page23.html page89.html page19.html page8.html page48.html page1.html
 + Path Length : 8
 + Visited 20 nodes, starting @ intranet7/page1.html, using: best search.

============== Task 2b ===============
intranet 1 :
 + Reverse path : page50.html page99.html page88.html page98.html page84.html page58.html page70.html page1.html
 + Path Length : 7
 + Visited 10 nodes, starting @ intranet1/page1.html, using: beam search.

intranet 5 :
 + Reverse path : page62.html page72.html page95.html page96.html page87.html page89.html page99.html page40.html page83.html page8.html page93.html page70.html page1.html
 + Path Length : 12
 + Visited 29 nodes, starting @ intranet5/page1.html, using: beam search.

intranet 7 :
 + Visited 9 nodes, starting @ intranet7/page1.html, using: beam search.

```

## result

- Key: \<number of nodes visited\> / \<solution-path length\>
- best and beam are selected be Hvalue.
- bean width is 2.

| Intranet#    | breadth     | depth    | best |   beam
| :------------- | :------ | :----- | :---- | :--- |
| Intranet1       | 91/4   |  58/15 | 26/7  | 10/7 |
| Intranet5       | 88/8   |  42/10 | 26/8  | 29/12 |
| Intranet7       | 56/6   |  12/6  | 20/8  | 9/- |


## discussion

### Task 2a)

**Question:** Is your heuristic admissible? Explain why or why not.

**Answer:** My heuristic function consist of 4 parts.
1. Percentage of all query words in one page.
2. Percentage of pattern query words in a hypertext.
3. Percentage of consecutive words in hypertext.
4. Score of the position of hypertext. (1 for the beginning, 0 for the endding)

I give them weights for 0.2, 0.3, 0.8, 0.2. And the summary are the H-value of one node.

I think the function is admissible. Because it provides correct choice for majority of situations. It is acceptable for human perceptions.

### Task 2c)

**Question:** How well did your heuristic work on the sample intranets?

**Answer:** My heuristic works well on Intranet1 and Intranet5. It reduced the cost (# of visited nodes) significantly. Meanwhile, the solution path increased only several steps. So, the performance is good.

However, the heuristic didn't work well when compared with depth search on Intranet7 and it is the only drawback case. Depth-first Search may get good solution with a little cost. But it does not guarantee the low-cost solution. Best-first Search with Beam didn't get valid solution on Intranet7. It is because the beam width is only 2. And we may discard the correct branch at the beginning of the process.  

## Future work

- does not implement task 3
