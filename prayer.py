#!/usr/bin/env python3

import EpistemicGraph

eg = EpistemicGraph.EG('prayer', 'png', False)

# Primary claim
primary_claim = 'God answers prayers through good feelings.'
primary = eg.node('none', primary_claim, [], primary=True)

# Sub claims
authority = eg.node('for', 'Scriptures/church taught me this.\nI trust them b/c of all the\ngood it\'s done for me.', [primary])
friends_family = eg.node('for', 'Friends and family have had\npowerful feelings through prayer.', [primary])
personal_good_feelings = eg.node('for', 'I have felt some good\nfeelings while praying.', [primary])

# Arguments against
#peer_pressure = eg.node('against', 'My feelings from prayer seem\ninfluenced by social pressure.', [personal_good_feelings])
internal_feelings = eg.node('against', 'Those good feelings\nare probably from myself.', [friends_family, personal_good_feelings])
good_vs_true = eg.node('against', 'Good things aren\'t necessarily true.\nThey can be wrong but still do good.', [authority])

# Retorts
stronger_feelings = eg.node('against', 'I\'ve had stronger good\nfeelings outside of prayer.', [personal_good_feelings])
endure = eg.node('against', 'You need to pray everyday.\nThere is something missing in your life.', [stronger_feelings])
try_again = eg.node('against', 'I still don\'t feel anything.\nWhen do I stop?', [endure])
eg.link('against', endure, try_again)
non_falsifiable = eg.node('against', 'It\'s impossible to test\nif those feelings came from god.\n(non-falsifiable)',
        [personal_good_feelings, friends_family])

# Title
eg.finish(f'\nArguments For & Against:\n{primary_claim}')
