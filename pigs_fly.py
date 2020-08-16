#!/usr/bin/env python3

import EpistemicGraph

eg = EpistemicGraph.EG('pigs_fly', 'png', True)

# Primary claim
primary_claim = 'Pigs can\'t fly.'
primary = eg.node('none', primary_claim, [], primary=True)

# Sub claims
visual = eg.node('for', 'I\'ve never seen a pig fly.', [primary])
wings = eg.node('for', 'Pigs don\'t have wings.', [primary])

# Arguments for/against
not_looking = eg.node('against', 'They only fly when you\'re not looking.', [visual])
other_methods = eg.node('against', 'There are other methods of flight\nor definitions of flying.', [wings])

unfalsifiable = eg.node('against', 'Seems hard or impossible to test.\nIs it not falsifiable?', [not_looking])

# Title
eg.finish(f'\nArguments For & Against:\n{primary_claim}')
