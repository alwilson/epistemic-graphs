#!/usr/bin/env python3

import EpistemicGraph

eg = EpistemicGraph.EG('prayer', 'png', True)

# Primary claim
primary_claim = 'God answers prayers through good feelings.'
primary = eg.node('none', primary_claim, [], primary=True)

# Sub claims
scriptural = eg.node('for', 'Scriptures and church\ntaught me this.', [primary])
eg.link('for', primary, scriptural)
friends_family = eg.node('for', 'Friends and family have had\npowerful feelings through prayer.', [primary])
personal_good_feelings = eg.node('for', 'I have felt some good\nfeelings while praying.', [primary])

internal_feelings = eg.node('against', 'Those good feelings\nare probably from myself.', [primary, personal_good_feelings])

# Arguments against
peer_pressure = eg.node('against', 'My feelings from prayer seem\ninfluenced by social pressure.', [personal_good_feelings])

# Retorts
stronger_feelings = eg.node('against', 'I\'ve had stronger good\nfeelings outside of prayer.', [personal_good_feelings])
endure = eg.node('against', 'You need to pray everyday.\nThere is something missing in your life.', [stronger_feelings])
try_again = eg.node('against', 'I still don\'t feel anything.\nWhen do I stop?', [endure])
eg.link('against', endure, try_again)
non_falsifiable = eg.node('against', 'It\'s impossible to\ntest if those feelings came from god.\n(non-falsifiable)',
        [personal_good_feelings, scriptural, friends_family])

# Title
eg.finish(f'\nArguments For & Against:\n{primary_claim}')
