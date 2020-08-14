#!/usr/bin/env python3

import EpistemicGraph

eg = EpistemicGraph.EG('evolution', 'png', True)

# Primary claim
primary_claim = 'Humans evolved from single-celled organisms, w/o a creator.'
primary = eg.node('none', primary_claim, [], primary=True)

# Sub claims
evidence = eg.node('for', 'Multiple sources of empiric evidence.\n(DNA mutations, fossil record, traits across species)', [primary])
tool_of_god = eg.node('against', 'Evolution is how god created man.', [primary])

# Arguments for/against
faith_trial = eg.node('against', 'Evidence was planted by god/satan', [primary])
science_low_confidence = eg.node('against', 'Science has been wrong before.', [primary])
wikipedia = eg.node('for', 'Wikipedia is mostly trustworthy.', [evidence],
        url='https://en.wikipedia.org/wiki/Human_evolution#Evidence')
non_falsifiable = eg.node('against', 'Non-Falsifiable', [tool_of_god, faith_trial])
non_falsifiable = eg.node('against', 'Science has been right before?', [science_low_confidence])


# Title
eg.finish(f'\nArguments For & Against:\n{primary_claim}')

