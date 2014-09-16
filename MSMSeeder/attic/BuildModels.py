#!/usr/bin/env python
#
# Models a set of targets sequences onto a set of template structures using Modeller.
#
# Daniel L. Parton <daniel.parton@choderalab.org> - 11 Mar 2014
#

import MSMSeeder
import MSMSeeder.attic.modelling

# ========
# Parse command-line arguments
# ========

import argparse
argparser = argparse.ArgumentParser(description='Models a set of target sequences onto a set of template structures using Modeller.', formatter_class=argparse.RawTextHelpFormatter)

argparser.add_argument('--targets', nargs='+', help='(Default: all targets) Optionally define a subset of targets to work on by providing one or more target IDs separated by spaces (e.g. "ABL1_HUMAN_D0")')
argparser.add_argument('--templates', nargs='+', help='(Default: all templates) Optionally define a subset of templates to work on by providing one or more template IDs separated by spaces (e.g. "ABL1_HUMAN_D0_1OPL_A")')
argparser.add_argument('-v', '--verbose', action='store_true', help='Verbose')
args = argparser.parse_args()

MSMSeeder.attic.core.check_project_toplevel_dir()

# ========
# Build models
# ========

MSMSeeder.attic.modelling.build_models(process_only_these_targets=args.targets, process_only_these_templates=args.templates, verbose=args.verbose)

# ========
# Write a list of models sorted by sequence identity
# ========

MSMSeeder.attic.modelling.sort_by_sequence_identity(process_only_these_targets=args.targets, verbose=args.verbose)

# ========
# Cluster models
# ========

MSMSeeder.attic.modelling.cluster_models(process_only_these_targets=args.targets, verbose=args.verbose)
