#!/usr/bin/env python3

import EpistemicGraph

eg = EpistemicGraph.EG('prayer', 'png', True)

# Primary claim
primary_claim = 'God answers prayers through good feelings.'
primary = eg.node('none', primary_claim, [], primary=True)

# Arguments for
scriptural = eg.node('for', 'The scriptures are evidence\nof how god answers prayers.\n(historical evidence)', [primary])
friends_family = eg.node('for', 'Friends/family have had\npowerful feelings through prayer.\n(personal experience)', [primary])
personal_good_feelings = eg.node('for', 'I have felt good\nfeelings while praying.\n(personal experience)', [primary])

# Arguments against
peer_pressure = eg.node('against', 'My feelings from prayer seem\ninfluenced by peer pressure.\n(doubt)', [primary])

# Retorts
stronger_feelings = eg.node('against', 'I\'ve had stronger good\nfeelings outside of prayer.\n(counter example)', [primary, personal_good_feelings])
endure = eg.node('against', 'You need to pray and read scriptures everyday.\nThere is something missing in your life preventing answers.\n(circular)', [stronger_feelings])
non_falsifiable = eg.node('against', 'It\'s difficult/impossible to\nprove those feelings came from god.\n(non-falsifiable)',
        [primary, personal_good_feelings, scriptural, friends_family])

# Title
eg.finish(f'\nArguments For & Against:\n{primary_claim}')
