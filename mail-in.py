#!/usr/bin/env python3

import EpistemicGraph

eg = EpistemicGraph.EG('mail-in', 'png', False)

# Primary claim
primary_claim = 'Mail-in voting is a good addition to in-person voting. (USA)'
primary = eg.node('none', primary_claim, []) #, primary=True)

# Arguments for/against

#improves_voting = eg.node('for', 'Improves voting overall', [primary])

higher_part = eg.node('for', 'Improves vote accuracy by\nincreasing in voter turnout.', [primary], url='https://www.politifact.com/article/2020/may/18/does-voting-mail-lead-higher-turnout-red-blue-and-/')
more_informed = eg.node('for', 'Voters take more time to be informed.\n(my experience)', [primary])

unknown_impact = eg.node('against', 'In-person voting is a\nfilter for informed voters.', [higher_part])
unknown_impact = eg.node('against', 'It could change vote\nshare in unknown ways.', [higher_part])
partison_turnout = eg.node('for', 'No impact on partisan vote share.', [unknown_impact], url='https://www.pnas.org/content/117/25/14052')

fraud = eg.node('against', 'Easier to commit fraud.', [primary])
not_ready = eg.node('against', 'Mail infrastructure is not prepared\nfor widespread mail-in voting.', [primary])

fud = eg.node('against', 'Hard to find evidence,\nbut solid concern.', [fraud])
partial = eg.node('against', 'Can still be implemented\npartially and within reason.', [not_ready])

# Title
eg.finish(f'\nArguments For & Against:\n{primary_claim}')

