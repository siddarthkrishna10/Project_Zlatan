# The Curious Case of Zlatan Ibrahimović

While working on my [Football Transfers piece](https://github.com/siddarthkrishna10/Football_Transfers), I came across a quirk in the dataset. _Zlatan Ibrahimović_; the legendary Journeyman/Illeist/Scorer-of-great-goals/Pompous/Swedish Footballer, was undervalued throughout his career. You would think that one of the most decorated footballers in the modern era who has won over 31 career trophies and scored over 450+ goals would've been highly sought after in terms of money! But that doesn't seem to be the case with Zlatan. Just take a look at this graph,

![ZlatanValuation_Snap](https://github.com/siddarthkrishna10/Project_Zlatan/blob/master/Code/ZlatanValuation_Snap.PNG)

Across the nine clubs he's played in, only F.C. Barcelona splashed a huge amount of money(€69.5 million) to get him and ironically his time there turned out to be a nightmare...of the field at least.

Here is the code snippet for the graph:
```python
#Reading the dataset into an object
a = pd.read_csv('https://github.com/siddarthkrishna10/Project_Zlatan/blob/master/Code/ZlatanStat_Sheet.csv')

#Plotting a bar graph for Market Value and Transfer Fee
a.plot(x='Club', y=['Market_Value', 'Transfer_Fee'], kind='bar')
plt.xlabel('Club')
plt.xticks(rotation=45)
plt.show()
```

Despite playing excellent football and banging in goals constantly at all the nine clubs he's played for, the market hasn't valued Ibrahimović highly. Even if you put aside the stats, his global superstar status and his bombastic attitude off the field didn't help. He's loved by millions for his eccentric and over-the-top attitude, helping him attain cult status in football but there is no clue as to why Zlatan is up there among the big-money players.

This simple project of mine is just me trying to analyse Zlatan Ibrahimović's club career with some charts to help us see how he has performed in each club and country he's played in.

> NOTE: The stats from his Malmö days are inaccurate and a lot of sources contradict each other. So I've decided to exclude Malmö from the majority of my analysis. I'll point it out if I include them.

Before I go any further, here is a table summarising Zlatan's club career:

Club | Period(Months) | Market Value | Transfer Fee | Appearances | Minutes Played | Goals | Assists
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: 
Malmö FF | 30 | €0 | €0 | 47 | NA | 18 | 3
Ajax | 37 | €0 | €7,800,000 | 110 | 7193 | 48 | 15
Juventus | 23 |  €0 | €16,000,000 | 92 | 6867 | 26 | 7
Internazionale | 36 | €25,000,000 | €24,800,000 | 117 | 9712 | 66 | 29
Barcelona | 13 |  €45,000,000 | €69,500,000 | 46 | 3334 | 22 | 13
A.C. Milan(Loan) | 10 |  €35,000,000 | €0 | 41 | 3394 | 21 | 12
A.C. Milan | 12 | €35,000,000 | €24,000,000 | 44 | 3807 | 35 | 12
Paris Saint-Germain | 48 | €37,000,000 | €21,000,000 | 180 | 15090 | 156 | 60
Manchester United | 21 |  €15,000,000 | €0 | 53 | 4034 | 29 | 10
LA Galaxy | 21 | €5,000,000 | €0 | 58 | 4933 | 53 | 15

Starting out at his home country with Malmö FF, playing his way up from the youth team and breaking into the first team in 1999, Zlatan has always been an out and out striker. There are no two ways about where he plays, he plays down the centre and upfront. He's a textbook goalscorer with a sharp eye for goal and amazing acrobatic skills - thanks to his Taekwando background.

From [transfermarkt](https://www.transfermarkt.com/) and other websites(which will be listed at the end), I've created a CSV sheet of the goals, appearances and minutes played for Zlatan at each club; from Malmö FF to LA Galaxy. _Remember...Malmö won't be included in my analysis due to the unavailability of accurate stats.

First thing I'd like to show is how Zlatan's faired in the countries he's played. Because if there is anything that defines a journeyman footballer, it's to show his exploits; how's he performed in the countries he's played in.

First, here is the code for plotting it:

```python
#Reading the dataset into an object
b = pd.read_csv('https://github.com/siddarthkrishna10/Project_Zlatan/blob/master/Code/Zlatan_ClubComp.csv')

#Plotting a pairplot for Appearances vs Goals and Minutes Played using Seaborn
b1 = sns.pairplot(b, y_vars=['Appearances'], x_vars=['Goals', 'Minutes_Played'], hue="Country")
plt.show()
```

The output graph for this is:

![ZlatanPairPlot_Snap](https://github.com/siddarthkrishna10/Project_Zlatan/blob/master/Code/ZlatanPairPlot1_Snap.PNG)

Just writing code and plotting graphs would seem mundane and anyone can do that. But I'd like to think that I do it for a reason, that I can extract some sort of story from it.

As with the above plot, we can see it has a tad bit of linearity to it. Goes to show that as he played more and more matches, the more goals he scored. Shows how consistent Zlatan Ibrahimović has been in putting it in the net. Not many footballers, let alone journeyman footballers can say that. Even at Barcelona, where he's said to have had a hard time with _Pep Guardiola_ and wasn't played more centrally than normal, he had 22 goals from 46 appearances which is great for a striker playing second fiddle to a certain young Argentinian sensation.

Now, you'd be asking why I plotted Appearances VS Minutes Played. Isn't it obvious that as a player's appearance increases, his minutes played also increases?

_Actually yes...but no!_

Strikers usually as they grow old, they tend to become super subs. Brought on in the last 10-20 mins to grab a late equaliser or winner for the team. So generally, a striker like Zlatan should've seen a decrease in his playing time as the years went by. But that wasn't the case,

![ZlatanPairPlot2_Snap](https://github.com/siddarthkrishna10/Project_Zlatan/blob/master/Code/ZlatanPairPlot2_Snap.PNG)

```python
#Reading the dataset into an object
c = pd.read_csv('https://github.com/siddarthkrishna10/Project_Zlatan/blob/master/Code/ZlatanStat_Sheet.csv')

#Dropping Malmö row from the dataframe object
c = c.drop([0])

#Converting Minutes_Played column from non-null object to a integar type
c['Minutes_Played'] = pd.to_numeric(c['Minutes_Played'])

#Calculating the Minutes Per Game
c['Minutes_PerGame'] = round(c['Minutes_Played']/c['Appearances'])

#Plotting for Appearances vs Minutes Per Game using Seaborn
cc3 = sns.pairplot(c, y_vars=['Appearances'], x_vars=['Minutes_PerGame'], hue="Club")
plt.show()
```

As you can see, apart from Ajax, he's got a steady playtime everywhere he went. Even his at his most recent club; LA Galaxy, he's been on the field 85 minutes per game...at the age of 37. Goes to show the fitness levels of Ibrahimović. Another great example showcasing his longevity was his speedy recovery during his _Red Devil_ days when he sustained serious ligament damage in his right knee only to come back into action six-and-half months later. Not only was scoring and playing beautiful football, but he also kept himself physically fit throughout his career.

Now for the last part, let's analyse Zlatan's league performance throughout his career. For this we'll take two new parameters into account; _Goals Per Game_ and _Minutes Per Goal_. I think that these two are self-explanatory from their names. Calculating them as plotting them in pairplots in my next step.

First, the code for that,

```python
#Calculating the Goals Per Game and Minutes Per Goal
b['Goals_PerGame'] = round(b['Goals']/b['Appearances'], 2)
b['Minutes_PerGoal'] = round(b['Minutes_Played']/b['Goals'])

#Taking only Zlatan's league stats into consideration
bb1 = b[b['Competition_Type'] == 'League']

#Plotting using seaborn for Appearances vs Goals Per Game and Minutes Per goal
bb2 = sns.pairplot(b, y_vars=['Appearances'], x_vars=['Goals_PerGame', 'Minutes_PerGoal'], hue="Club")
plt.show()
```

And this is the graph,

![ZlatanPairPlot3_Snap](https://github.com/siddarthkrishna10/Project_Zlatan/blob/master/Code/ZlatanPairPlot3_Snap.PNG)

This chart infact proves beyond any doubt that Zlatan has been a great player whereever he went. To be more elaborate; notice the vague chirality between the left and right graphs in the above pairplot. The left graph shows that as he appeared in more matches, he scored more goals as his goals per game ratio increases and the right graph shows that as he played in more league matches, the minutes between two goals(Minutes Per Goal) reduces; meaning he scored more frequently as the days went by.

I'm sorry if I sound like a broken recorder, but the stats don't lie! Zlatan Ibrahimović has been consistent throughout his club career. 

## Conclusion:

I started off this piece by wondering why Zlatan had been so undervalued throughout his career and after all these graphs, it's only made that question a lot tougher to answer. It's an enigma as to why he wasn't big in the market and was moved around a lot. But nothing seems to have stopped him from scoring. He started in Malmö and he still banged them in constantly in Los Angeles until recently.

The only layman's reason I or any other knowledgeable football fan could come up with is his **age**. As he grew old, clubs kept selling him for a bargain price and every single time he's proven himself the player he is. I believe that on some level, these clubs do regret not using him to his full potential.

As mentioned in my other project, age is a big factor when it comes to the valuation of a player. Young players are usually valued higher than their older counterparts even if the said old player has proven himself. And that's been the case with Zlatan ever since his Barcelona exit. Even in 2012, when Paris Saint-Germain was drowning in brand new oil money, they got him below the market value price(€21 million). 

_Andrea Pirlo_ is a great example for citing age playing a role in transfer. The Italian playmaker played some of his best football when he moved from A.C. Milan to Juventus in 2011 on a free transfer at the age of 31. A.C. Milan didn't think that Pirlo could contribute anymore with him hitting the 30s and decided not to renew his contract. Juventus pounced on _Il professore_ who went on to play some scintillating, if not magical, football for _The Old Lady_.

I think this has been the case for Zlatan throughout his post-_Inter_ career. Every club he's been to, he's scored goals, won them accolades and yet every future club decides he isn't worth the big bucks. Like I mentioned earlier, it could be his age or the fact that he is a bit of a character to deal with in the dressing room...we may never know.

_As of November 30th, his market value stands at €3.5 million. No one knows which league or country Zlatan Ibrahimović is planning to go next. But one thing's for sure...wherever he ends up, he'll sure be in the spotlight...on and off the field!_

### Sources:
- https://www.transfermarkt.com/zlatan-ibrahimovic/profil/spieler/3455
- https://en.wikipedia.org/wiki/Zlatan_Ibrahimovi%C4%87
- https://fbref.com/en/players/4cde5509/Zlatan-Ibrahimovic
- http://www.zlatanibrahimovic.com/the_career/the_ztatistics
