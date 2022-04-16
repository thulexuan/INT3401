# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    1. tao 1 stack, cac phan tu cua stack gom trang thai vaf hanh dong de dat duoc trang thai do
    2. tao 1 list cac node da duoc tham visited_nodes
    3. them node ban dau vao stack. neu node do la trang thai ket thuc --> return
    4. them node do, hanh dong de co node do (ban dau la rong) vao stack
    5. while stack khong rong
      5.1. currentState, actions_list = stack.pop
      5.2. kiem tra xem co trong visited_nodes chua
      5.3. kiem tra xem la trang thai ket thuc chua
      5.4. neu chua phai ket thuc, duyet cac trang thai tiep theo cua currentState, them vao stack

    """


    start_state = problem.getStartState()

    stack = util.Stack()
    visited_nodes = []
    stack.push((start_state,[]))
    while not stack.isEmpty():
        current_state, actions_list = stack.pop()
        if current_state not in visited_nodes:
            visited_nodes.append(current_state)
            if (problem.isGoalState(current_state)):
                return actions_list
            for next_state, action, cost in problem.getSuccessors(current_state):
                next_actions_list = actions_list + [action]
                stack.push((next_state, next_actions_list))

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first.
       Tuong tu nhu ham depthFirstSearch, bfs dung Queue thay vi Stack
    """
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()

    queue = util.Queue()
    visited_nodes = []
    queue.push((start_state, []))
    while not queue.isEmpty():
        current_state, actions_list = queue.pop()
        if current_state not in visited_nodes:
            visited_nodes.append(current_state)
            if (problem.isGoalState(current_state)):
                return actions_list
            for next_state, action, cost in problem.getSuccessors(current_state):
                next_actions_list = actions_list + [action]
                queue.push((next_state, next_actions_list))
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first.
    ucs duyet node co chi phi thap nhat --> Dung priorityQueue, moi phan tu cua priorityQueue gom bo ba
    tra ve tu ham getSuccessors va do uu tien
    Dung PriorityQueue de xoa phan tu co do uu tien thap nhat (chi phi thap nhat)
    """
    "*** YOUR CODE HERE ***"

    start_state = problem.getStartState()


    priorityQueue = util.PriorityQueue()
    visited_nodes = []
    priorityQueue.push((start_state, [], 0), 0)
    while not priorityQueue.isEmpty():
        current_state, actions_list, current_cost = priorityQueue.pop()
        if current_state not in visited_nodes:
            visited_nodes.append(current_state)
            if problem.isGoalState(current_state):
                return actions_list
            for next_state, action, cost in problem.getSuccessors(current_state):
                new_actions_list = actions_list + [action]
                new_cost = current_cost + cost
                priorityQueue.push((next_state, new_actions_list, new_cost), new_cost)

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first.
    Dung PriorityQueue, cho do uu tien cong them ham heuristic
    """

    "*** YOUR CODE HERE ***"

    start_state = problem.getStartState()


    visited_nodes = []
    priorityQueue = util.PriorityQueue()
    priorityQueue.push((start_state, [], 0), 0)

    while not priorityQueue.isEmpty():
        current_state, actions_list, current_cost = priorityQueue.pop()
        if current_state not in visited_nodes:
            visited_nodes.append(current_state)
            if problem.isGoalState(current_state):
                return actions_list
            for next_state, action, cost in problem.getSuccessors(current_state):
                new_actions_list = actions_list + [action]
                priority = current_cost + cost + heuristic(next_state, problem) #A* co ham danh gia cong them ham kinh nghiem heuristic
                new_cost = current_cost + cost
                priorityQueue.push((next_state, new_actions_list, new_cost), priority)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
