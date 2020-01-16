# Task1: Programming Practice

**Name:** Kai Yang
**Degree:** BA
**ID:** 20640696

## Problem 1 - Creating and Transforming Array

```matlab
% Create M1 matrix
consec = 1:64;
M1 = reshape(consec, [8,8]);

% Create M2 matrix
M2 = transpose(M1);

% Create M3 matrix
M3 = M1;
M3(1:4,1:4) = 1;

% Create M4 matrix
M4 = M1;
M4(4:5,4:5) = 0;

% Create M5 matrix
M5 = M1;
for ii = 1:2:7
    M5(ii:ii+1, ii:ii+1) = 1;
end

% Create M6 matrix
M6 = fliplr(M1);
for ii = 1:2:7
    M6(ii:ii+1, ii:ii+1) = 1;
end
M6 = fliplr(M6);

% Create M7 matrix
M7 = M1;
for ii = 1:2:7
    M7(ii:ii+1, ii:ii+1) = 0;
end

% Create M8 matrix
M8 = M1
M8_mask = zeros(8);
for ii = 1:2:7
    M8_mask(ii:ii+1, ii:ii+1) = 1;
end
M8(~M8_mask) = 100;

% Create M9 matrix
M9 = M8;
M9(find(M9==100)) = 0;
```

## Problem 2 - Bulls and Cows

```matlab
% Placeholder vectors to track the values of true and test case numbers
true_num_seq = zeros(1,10);
test_num1_seq = zeros(1,10);
test_num2_seq = zeros(1,10);

true_num_seq(true_num + 1) = 1;
test_num1_seq(test_num1 + 1) = 1;
test_num2_seq(test_num2 + 1) = 1;

% Compute number of bulls and cows
bull1 = sum(true_num == test_num1)
cow1 = sum(and(true_num_seq == 1, test_num1_seq == 1)) - bull1

bull2 = sum(true_num == test_num2)
cow2 = sum(and(true_num_seq == 1, test_num2_seq == 1)) - bull2

```


## Problem 3 - Poker Game

```matlab
% Check if your card ranking is Royal Flush
function is_ryl_str_fls = ChckRylFls(cards)
% Create an array to represent a matrix with same shape as a deck
deck = zeros(1,52);
deck(cards) = 1;
deck = transpose(reshape(deck,[4,13]));

% Zero out the matrix of non-royal flush cards
deck(2:9, 1:4) = 0;

% Sum the columns
suit_sums = sum(deck);

% Check royal flush condition
if ismember(1, suit_sums > 4)
    is_ryl_str_fls = true;
else
    is_ryl_str_fls = false;
end

end

% Check if your card ranking is Straight Flush
function is_str_fls = ChckStrFls(cards)
% Create an array to represent the deck of cards 
deck = transpose(reshape(1:52, [4,13]));

% Straight flush requires 5 cards of the same suit
suit = rem(cards,4);
if sum(suit == 1) < 5 && sum(suit == 2) < 5 && sum(suit == 3) < 5 && sum(suit == 0) < 5
    % If there are less than 5 cards from a suit, flush impossible
    is_str_fls = false;
else
    % Determine which suit is the dominant suit
    main_suit = mode(suit);
    if main_suit == 0
        main_suit = 4;
    end
    
     % Get a vector of the cards from the main suit (ie. clubs or diamonds)
    main_suit_cards = deck(:,main_suit);
    
    % Remove the cards in the hand that is not part of the main suit
    remove_cards = setdiff(cards, main_suit_cards);
    cards = setdiff(cards, remove_cards);
    
    % Determine the value of the cards
    cards = ceil(cards/4);
    
    % Determine the index of the cards
    card_instances = zeros(1,13);
    card_instances(cards) = 1;
    
    % Check if you have 5 consecutive values in your hand
    consec_cards = diff([0 find(diff(card_instances)) numel(card_instances)]);
    if card_instances(1) == 1
        consec_cards = consec_cards(1:2:end);
    else
        consec_cards = consec_cards(2:2:end);
    end
    
    max_consec_cards = max(consec_cards);
    
    % Check straight flush conditions
    if max_consec_cards > 4
        is_str_fls = true;
    else 
        is_str_fls = false;
    end
end

end

% Check if your card ranking is Four of a Kind
function is_fr_knd = ChckFrKnd(cards)
% Create an array to represent a matrix with same shape as a deck
deck = zeros(1,52);
deck(cards) = 1;
deck = transpose(reshape(deck,[4,13]));

% Sum the rows of the deck matrix to find num cards having the same value
num_cards_per_value = sum(deck');

% Check 4 of a kind condition
if ismember(4,num_cards_per_value)
    is_fr_knd = true;
else
    is_fr_knd = false;
end

end

% Check if your card ranking is Full House
function is_fll_hs = ChckFllHs(cards)
% Create an array to represent a matrix with same shape as a deck
deck = zeros(1,52);
deck(cards) = 1;
deck = transpose(reshape(deck,[4,13]));

% Sum the rows of the deck matrix to find num cards having the same value
num_cards_per_value = sum(deck');

% Check full house condition
if ismember(3, num_cards_per_value) && ismember(2, num_cards_per_value)
    is_fll_hs = true;
else
    is_fll_hs = false;
end

end

% Check if your card ranking is Flush
function is_fls = ChckFls(cards)
% Create an array to represent a matrix with same shape as a deck
deck = zeros(1,52);
deck(cards) = 1;
deck = transpose(reshape(deck,[4,13]));

% Sum the columns to find the number of cards per suit
num_cards_per_suit = sum(deck);

% Check the flush condition
if ismember(1, num_cards_per_suit > 4)
    is_fls = true;
else
    is_fls = false;
end

end

% Check if your card ranking is Straight
function is_str = ChckStr(cards)
% https://www.mathworks.com/matlabcentral/answers/114852-finding-consecutive-true-values-in-a-vector
card_vec = zeros(52,1);
card_vec(cards) = 1;
card_mat = reshape(card_vec, 4, []);

% 'A' become either 1 or 14. Thus, the first column in 'card_mat' is added
% to the end+1 column in 'card_mat'.
card_mat = [card_mat card_mat(:,1)];

card_sum = sum(card_mat); % sum cards in column direction

card_num = find(card_sum~=0); % find columns that have at least one of
% that card type - returns the index where that column is (card number)

str_ind = strfind(diff(card_num), [1 1 1 1]);
% Straight must have five consecutive card numbers. Take the differece
% between each element and the element after Look for anywhere that the
% difference between the two cards is 1 (shows they are consecutuive) the
% difference between 5 cards should be 1 four consecutive times search if
% [1 1 1 1] is in your str_ind vector - if it is, is_str = true

is_str = ~isempty(str_ind);
end

% Check if your card ranking is Three of a Kind
function is_thr_knd = ChckThrKnd(cards)
% Create an array to represent a matrix with same shape as a deck
deck = zeros(1,52);
deck(cards) = 1;
deck = transpose(reshape(deck,[4,13]));

% Sum the rows of the deck matrix to find num cards having the same value
num_cards_per_value = sum(deck');

% Check the condition for three of a kind
if ismember(3, num_cards_per_value)
    is_thr_knd = true;
else 
    is_thr_knd = false;
end

end

% Check if your card ranking is Two Pairs
function is_tw_prs = ChckTwPrs(cards)
% Create an array to represent a matrix with same shape as a deck
deck = zeros(1,52);
deck(cards) = 1;
deck = transpose(reshape(deck,[4,13]));

% Sum the rows of the deck matrix to find num cards having the same value
num_cards_per_value = sum(deck');

% Check two pair conditions
num_pairs = num_cards_per_value == 2;
if sum(num_pairs) > 1
    % Simply checking if there is more than 1 pair. it is possible to have
    % 3 pairs in the 7 cards, in which case, it would still count as two
    % pair in poker
    is_tw_prs = true;
else
    is_tw_prs = false;
end

end

% Check if your card ranking is Pair
function is_pr = ChckPr(cards)
card_vec = zeros(52,1);
card_vec(cards) = 1;
card_mat = reshape(card_vec, 4, 13);
% create 4x13 matrix where each row is equal to a different suit and each
% column is equal to a different card number. For example, the first column
% is 1 (Ace), the second column is 2, and so on.

card_sum = sum(card_mat);

is_pr = any(card_sum==2);
% check if there is a column that has exactly two cards is a pair
end
```
