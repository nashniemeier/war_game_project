<h1><b>War Game Research Project: A Monte Carlo Study of Initial Deal Effects</b></h1>
<h3>Author: Nash Niemeier</h3>
<br>
<h2>Problem Statement:</h2>
<p>This project investigates whether properties of the initial deal in the two-player card game War influence probabilistic outcomes such as win likelihood, game length, and the number of wars. Although War is commonly regarded as a game of pure chance, the initial deal fully determines the probability space over all possible game outcomes.

A common intuition is that controlling high-value cards, such as aces, guarantees victory; however, this reasoning overlooks the role of wars, which introduce additional randomness and can cause a player to lose multiple cards in a single event. This project examines whether measurable features of the initial deal provide statistically meaningful information about expected outcomes, despite the game’s inherent stochasticity.</p>

<h2>Why this Problem is Interesting:</h2>
<p>This problem is interesting to study because War is commonly regarded as a game of pure luck, with many assuming that the outcome is effectively determined by the initial deal. However, closer examination of the game mechanics—particularly the reshuffling of a player’s deck after it is exhausted—reveals additional layers of randomness that influence the progression and outcome of a game.

By analyzing measurable properties of the initial deal and their relationship to probabilistic outcomes, this project explores whether meaningful structure exists beneath the game’s apparent randomness. More broadly, this mirrors real-world systems in which outcomes are shaped by both deterministic initial conditions and stochastic processes. As a data science project, this serves as a clear demonstration of how multiple parameters can influence outcomes in systems dominated by chance.</p>

<h2>Variables and Definitions</h2>
<h3>The following variables represent <u><b>outcomes</b></u> of a completed game of War and are treated as random variables</h3>
<p>
- Winner: determined by who controls all cards measured at the end of the game.<br>
- Game Length: defined by the total number of rounds until one player has all cards, one round is one card played by each player.<br>
- Number of wars: defined as the number of rounds in which both players reveal cards of equal rank, triggering a war.<br>
- Number of reshuffles per player: defined by the total number of times each player has to reshuffle.<br>
</p>
<h3>The following variables represent <u><b>inputs</b></u> before a game of War and are treated as random variables</h3>
<p>
- Difference in # of high cards (Jack-Ace): the difference between the number of high cards that player A has versus player B, showing if a player has an advantage over the other.<br>
- Difference in average + STD card rank: The difference between Player A and Player B in average card value, with standard deviation measuring spread. This captures overall deck quality and variability, providing insight beyond mean rank.<br>
- Difference in number of low cards (2-5): the difference between the number of low cards that Player A has versus Player B. This shows if a player starts the game with a disadvantage.<br>
</p>
<h3>The following describes the <u><b>Experimental Structure</b></u> of the experiment</h3>
<p> <b>For this experiment, using two tables is the best option</b><br>
- Initial Deal Table: Each row corresponds to one initial deal. Columns include per-player statistics (high cards, average rank, standard deviation) and the computed differences for ease of analysis.<br>
- Game Outcomes Table: Each row corresponds to a single game played from a specific initial deal. Each initial deal is simulated 50 times, resulting in 50 outcome rows per deal. Columns include variables such as winner, number of wars, and number of rounds (where each round represents one card flipped by each player).<br>
</p>

<h2>Experimental Design</h2>
<h3>Procedure:</h3>
1. The initial deal of a 52-card deck is generated and split between two players. Statistics listed in <u>inputs</u> are recorded.
2. Each initial deal is simulated 50 independent times, with full reshuffling whenever a player runs out of their play deck. This gives randomness during gameplay.
3. For each game, the <u>outcomes</u> listed above are recorded.
4. 200 unique initial deals are generated, 50 games per deal, with random shuffles done each time.

<h3>Stopping Criteria</h3>
- Simulation will continue until each initial deal is simulated 50 times
- Win probability estimates stabilize within a 5% tolerance

<h2>Biases & Limitations</h2>
1. Variance in deals may not always be prominent, as random deals tend to cluster around an average card value
2. Extreme games that go long may disproportionately affect the game length statistic
3. Results describe probabilistic trends, not deterministic predictions

<h2>Statistical Analysis Plan</h2>
<h3>Intent:</h3>
<p>The Goal of the statistical analysis is to quantify how properties of the initial deal influence probabilistic game outcomes, and to determine whether observed differences are statistically significant rather than coincidence</p>
<h3>Strategy:</h3>
<p>For <b>Win Probability</b>, our experiment</p>

- is binary
- uses large samples
- measures proportions
<p>A <b><u>Z-test</u></b> for difference in proportions is our best method to test for statistical significance</p>

<p>For <b>Game Length</b>, our experiment</p>

- Uses large samples
- Compares between two types of samples
<p>A <b><u>Two Sample Z-test</u></b> for difference in proportions is our best method to test for statistical significance</p>

<h4>For ALL testing,  &#945; = 0.05</h4>

<h4>Statistical significance is interpreted as evidence of <b>association</b>, NOT causation. Observed effects reflect shifts in outcome probabilities rather than deterministic guarantees.</h4>

<h2>Assumptions</h2>

<p>This analysis assumes that all deck shuffles are fair and uniformly random, and that players follow the rules of War without strategic decision-making. Each simulated game is treated as independent, including repeated games derived from the same initial deal, with outcome variability arising solely from reshuffling and war events.

Card ranks are mapped to numerical values using a linear scale for the purpose of computing averages and variability, providing a consistent but simplified representation of deck strength. Initial deals are grouped by feature differences under the assumption that such grouping reduces noise without obscuring meaningful structure.

Statistical inference relies on large-sample approximations, allowing the use of normal-based confidence intervals and hypothesis tests. All findings are interpreted as probabilistic associations rather than causal or deterministic claims.</p>

<h2>Expectations (Pre-Results)</h2>
<p>Prior to analysis, several qualitative trends are expected based on the mechanics of the game. Win probability is expected to increase approximately linearly as the difference in high-card count between players increases, with a midpoint near 50% when both players have similar initial strength. This relationship is expected to be symmetric, such that advantages favoring either player produce mirrored effects on win probability.

Game length is expected to increase as initial deals become more balanced in terms of average card rank and rank variability. When neither player has a clear advantage, outcomes should fluctuate more frequently, leading to longer games. Conversely, large imbalances in initial deal strength are expected to produce shorter games.

The number of wars is expected to increase when both players have low variability in card ranks, as more similar card values increase the likelihood of ties. In contrast, high variability in card ranks may reduce the frequency of wars by producing more decisive rounds.

In cases of extreme initial advantage, games are expected to exhibit fewer wars, shorter durations, and reduced variability across repeated simulations. Overall, effects are expected to vary smoothly across feature differences rather than exhibit abrupt thresholds; sharp discontinuities would suggest implementation artifacts rather than underlying game structure.</p>

<h2>Reproducibility and Project Structure</h2>
<p>To ensure reproducibility, all randomness in the experiment is explicitly controlled and logged. Initial deals are generated using a fixed random seed and assigned unique identifiers. For each initial deal, multiple independent games are simulated using distinct shuffle sequences, allowing outcome variability to be attributed solely to gameplay randomness rather than differences in the starting configuration.

Data generated by the simulations are stored in a structured relational format. One table records statistics derived from each initial deal, while a second table records outcomes from individual games linked to their corresponding initial deal. This separation enables clear traceability from initial conditions to observed outcomes and prevents feature leakage during analysis.

The project is organized to separate simulation logic, data storage, and analysis. Simulation components are responsible only for game execution and data generation, while analysis components operate exclusively on recorded data. This modular structure allows the experiment to be extended, replicated, or modified without altering previously generated results.</p>

<h2>Experimental Rules</h2>
- Each user starts with 26 cards, randomly shuffled and dealt between the two players
- 1 round consists of 1 card played
  - In the case of a war, 1 war is 1 round played
- A player wins when one of the following occurs:
  - They control all the cards
  - Their opponent does not have enough cards for a war
- Card suit does not matter, only their rank
- A war occurs when the same rank of card is played (Ex/ Both play a 6)
- In the case of a war, the following will occur:
  - Each player will draw three cards
  - The third card each player draws will be compared
  - The higher card wins the 6 cards from the war AND the 2 cards that tied
- When a player runs out of cards in their play deck, they will shuffle the winnings pile and that will become the new play deck

