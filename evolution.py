#!/usr/bin/env python3

import EpistemicGraph

eg = EpistemicGraph.EG('evolution', 'png', False)

# Primary claim
primary_claim = 'Humans evolved from single-celled organisms via natural selection.'
primary = eg.node('none', primary_claim, [], primary=True)

# Sub claims
evidence = eg.node('for', 'Multiple sources of empiric evidence.\n(DNA mutations, fossil record, traits across species)', [primary],
        url='https://en.wikipedia.org/wiki/Human_evolution#Evidence')
tool_of_god = eg.node('against', 'Evolution is how god created man.', [primary])

# Arguments for/against
faith_trial = eg.node('against', 'Evidence was planted by god/satan', [evidence])
science_low_confidence = eg.node('against', 'Science has been wrong before.', [primary])
non_falsifiable = eg.node('against', 'It\s impossible to prove that wrong.\n(Non-Falsifiable)', [faith_trial])
diff_claim = eg.node('against', 'Not really an argument\nbut a different claim.', [tool_of_god])
science_case_by_case= eg.node('against', 'Science has been right before?\nI evaluate on a case-by-case basis.', [science_low_confidence])

# Title
eg.finish(f'\nArguments For & Against:\n{primary_claim}')

