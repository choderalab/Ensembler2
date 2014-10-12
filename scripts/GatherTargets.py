#!/usr/bin/env python
#
# Gathers protein target data - IDs and sequences.
#
# Daniel L. Parton <daniel.parton@choderalab.org> - 11 Mar 2014
#

import MSMSeeder
import MSMSeeder.attic.initproject

# ========
# Parse command-line arguments
# ========

import argparse
argparser = argparse.ArgumentParser(description='Gather target protein data - IDs and sequences.', formatter_class=argparse.RawTextHelpFormatter)

helpstring_gatherfrom = r'''Choose a method for gathering target data.

"TargetExplorerDB": Gather target data from an existing TargetExplorer
database, specified via either the project metadata file or the --db_path
argument.

"UniProt": Gather target data from UniProt with a user-defined query
string.'''
argparser.add_argument('--gather_from', type=str, help=helpstring_gatherfrom, choices=['TargetExplorerDB', 'UniProt'])
argparser.add_argument('--db_path', type=str, help='TargetExplorerDB database path. Will be converted to an absolute path.', default=None)
args = argparser.parse_args()

MSMSeeder.attic.core.check_project_toplevel_dir()

# ========
# Parse project metadata
# ========

project_metadata = MSMSeeder.attic.core.ProjectMetadata()
project_metadata.load(MSMSeeder.attic.core.project_metadata_filename)

# ========
# Get the target selection method
# ========

# Command-line args take priority
target_selection_method = args.gather_from

# Otherwise check project metadata file
if target_selection_method == None:
    target_selection_method = project_metadata.get(('target-selection', 'target-selection-method'))

if target_selection_method == None:
    raise Exception, 'Target selection method not found in command-line args or in project metadata file. Cannot continue'

# ========
# Get method-specific parameters
# ========

if target_selection_method == 'TargetExplorerDB':

    # Command-line args take priority
    DB_path = args.db_path

    # Otherwise check project metadata file
    if DB_path == None:
        DB_path = project_metadata.get(('target-selection', 'TargetExplorer-database-path'))

    if DB_path == None:
        raise Exception, 'Database path not found in command-line args or in project metadata file. Cannot continue'

elif target_selection_method == 'UniProt':
    pass


# ========
# Run the selected gather targets method
# ========

if target_selection_method == 'TargetExplorerDB':
    MSMSeeder.attic.initproject.gather_targets_from_TargetExplorerDB(DB_path)

elif target_selection_method == 'UniProt':
    MSMSeeder.attic.initproject.gather_targets_from_UniProt()

