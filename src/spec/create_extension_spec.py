# -*- coding: utf-8 -*-
import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec
# TODO: import other spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc="""NWB extension for SWAC project in Harvey Lab""",
        name="""ndx-harvey-swac""",
        version="""0.1.0""",
        author=list(map(str.strip, """Shih-Yi Tseng""".split(','))),
        contact=list(map(str.strip, """shihyitseng41@gmail.com""".split(',')))
    )

    # TODO: specify the neurodata_types that are used by the extension as well
    # as in which namespace they are found.
    # this is similar to specifying the Python modules that need to be imported
    # to use your new data types.
    # all types included or used by the types specified here will also be
    # included.
#     ns_builder.include_type('ElectricalSeries', namespace='core')
    ns_builder.include_type('LabMetaData', namespace='core')

    # TODO: define your new data types
    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb
    # for more information
#     tetrode_series = NWBGroupSpec(
#         neurodata_type_def='TetrodeSeries',
#         neurodata_type_inc='ElectricalSeries',
#         doc=('An extension of ElectricalSeries to include the tetrode ID for '
#              'each time series.'),
#         attributes=[
#             NWBAttributeSpec(
#                 name='trode_id',
#                 doc='The tetrode ID.',
#                 dtype='int32'
#             )
#         ],
#     )
    
    labmetadata_ext = NWBGroupSpec(
        name='harvey_lab_swac_metadata',
        doc='extension type for storing harvey lab swac metadata metadata',
        neurodata_type_def='LabMetaDataSession',
        neurodata_type_inc='LabMetaData',
    )
    
    labmetadata_ext.add_group(
        name='TaskParam',
        doc='Parameters of the Virmen maze and task structure',
        attributes=[
            NWBAttributeSpec(
                name='maze_stem_length',
                doc='The length of the maze stem in Virmen unit',
                dtype='float',
            ),
            NWBAttributeSpec(
                name='maze_stem_width',
                doc='The width of the maze stem in Virmen unit',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='maze_arm_length',
                doc='The length of the maze arm in Virmen unit',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='maze_arm_width',
                doc='The width of the maze arm in Virmen unit',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='cue_delay_length',
                doc='The length of the cue delay (before the maze arms) in Virmen unit',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='wall_height',
                doc='The height of the maze walls in Virmen unit',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='max_position',
                doc='The maximum forwar position that the maze extends (hideCuePast) in Virmen unit',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='frac_non_visually_guided_trials',
                doc='The fraction of non visually guided trials',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='choice_bias_penalty',
                doc='The choice bias penalty',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='feedback_delay_sec',
                doc='The length of the feedback delay in seconds',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='reward_delay_sec',
                doc='The length of the reward delay in seconds',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='iti_correct_sec',
                doc='The length of inter-trial intervals in seconds for correct trials',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='iti_incorrect_sec',
                doc='The length of inter-trial intervals in seconds for incorrect trials',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='switches',
                doc='Trial number when a rule switch happened',
                dtype='int',
                shape=(None,)
            ),
            NWBAttributeSpec(
                name='initial_rule',
                doc='The rule of the first block',
                dtype='text'
            )
        ],
    ) 
    
    labmetadata_ext.add_group(
        name='AAVretroInjSite',
        doc='Injection sites of the AAVretro',
        attributes=[
            NWBAttributeSpec(
                name='mTagBFP2',
                doc='Injection sites for AAV2retro-Syn-mTagBFP2',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='mScarlet',
                doc='Injection sites for AAV2retro-Syn-mScarlet',
                dtype='text'
            )
        ],
    )
    
    labmetadata_ext.add_group(
        name='Imaging',
        doc='Information of calcium imaging',
        attributes=[
            NWBAttributeSpec(
                name='imaging_type',
                doc='Imaging type: plane or volume',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='num_of_frame_per_volume',
                doc='Number of frames per volume (the last frame is fly-back)',
                dtype='int'
            ),
            NWBAttributeSpec(
                name='num_of_imaging_plane',
                doc='Number of imaging plane',
                dtype='int'
            ),
            NWBAttributeSpec(
                name='cortical_layer',
                doc='Cortical layer of the imaging FOV',
                dtype='text'
            )
        ],
    )

    labmetadata_ext.add_group(
        name='Registration',
        doc='Information of registrating imaging FOV to CCF',
        attributes=[
            NWBAttributeSpec(
                name='fov_center_area',
                doc='FOV center area',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='fov_center_ml_ccf_mm',
                doc='FOV center location along ML axis in CCF (mm from bregma)',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='fov_center_ap_ccf_mm',
                doc='FOV center location along AP axis in CCF (mm from bregma)',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='fov_depth_mm',
                doc='Depth of the FOV top plane (mm below pia)',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='fov_plane_step_size_mm',
                doc='Step size between imaging planes in mm for volume imaging',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='fov_to_ccf_transformation_matrix',
                doc='Transformation matrix for transforming a column vector of FOV pixel coordiate ([x,y,1].T) to [ml, ap, _] in mm in CCF',
                dtype='float',
                shape=(3,3),
            )
        ],
    )
    
    
    # TODO: add all of your new data types to this list
    new_data_types = [labmetadata_ext]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)
    print('Spec files generated. Please make sure to rerun `pip install .` to load the changes.')


if __name__ == '__main__':
    # usage: python create_extension_spec.py
    main()
