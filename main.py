import numpy as np
import pya
import os
import mask_frontend as mask_f
import mask_backend as mask_b
import mask_pya_aip as mpa


def generate_pls_file(mask_object):
    file_ref = open("pls_reference_file.txt", "r")
    path = os.path.join( "..", "gds", "V1", mask_object.mask_name + "_test.pls")
    file_pls = open(path, "w")
    header = file_ref.read()
    file_ref.close()
    file_pls.write(header)

    i = 0

    ID = i
    X = 25.891829
    Y = 2.689630
    Z = 28.999800
    R = 0.000000
    T = 0.000000
    U = 25.891829
    V = 2.689630
    W = 7.544100
    Attribute = "A"
    Template = "XY"
    Comment = "Go to Farraday cup"
    # "STAY;"
    Options = ""
    # "VICOL" "MACRO" "ALWF_AUTO" "EXPOSURE"
    Type = ""
    # Size of the patterinig of of an image scan
    Size_U = ""
    Size_V = ""
    # Number of points of a image scan
    Points_U = ""
    Points_V = ""
    # Direction of the scan "U"
    Dir = ""
    # Number of avarages
    Avg = ""
    # At patterning 100.000 for pos1 and pos2
    Pos1 = ""
    Pos2 = ""
    Pos3 = ""
    Link = ""
    # file directory of name of the column settings
    File = ""
    # Layer span or number of the column ID mode
    Layer = ""
    # Working arease size 1100.000;1100.000;8900.000;9100.000
    Area = ""
    # Dose factor
    DoseFactor = ""
    # Dwell time in ms
    Dwelltime = ""
    Stepsize = ""
    SplDwell = ""
    SplStep = ""
    CurveStep = ""
    CurveDwell = ""
    DotDwell = ""
    FBMSArea = ""
    FBMSLines = ""
    # SplDot 44 at patterning why?
    SplDot = ""
    Time = ""
    Timestamp = ""
    Method = ""
    Dot = ""
    # auto WF align with images 0
    Angle = ""
    # auto WF align with images 255
    MarkSequences = ""
    # auto WF align with images 1
    Frame = ""
    # auto WF align with images 1
    LAvg = ""
    # patterning 0.016
    StepsizeU = ""
    StepsizeV = ""
    CurveLine = ""

    file_pls.write( str(i) + ",")

    file_pls.close()


def generate_lay_file(mask_object):
    file = open("lay_reference_file.txt", "r")
    path = os.path.join( "..", "gds", "V1", mask_object.mask_name + ".lay")
    file2 = open(path, "w")
    header = file.read()
    file.close()
    file2.write(header)


    for li in mask_object.layout.layer_indices():
        number = mask_object.layout.get_info(li)
        name = mask_object.layout.get_info(li).name
        file2.write( str(number.layer))
        file2.write( "=")
        file2.write( name)
        file2.write( ",")

        file2.write( str(li))
        file2.write( ",")
        file2.write( str(li))
        file2.write( ",")
        file2.write( str(7*(li%2)))
        file2.write( ",")
        
        file2.write( str(number.layer))
        file2.write( ",")

        file2.write( "1")
        file2.write( ",")
        file2.write( "1")
        file2.write( ",")
        file2.write( "1000")
        file2.write( ",")
        file2.write( "")
        file2.write( ",")
        file2.write( "-1")

        file2.write( "\n")
    
    file2.close()

class mask_paramters():

    def build_layers(self):
        self.layout.layer( 110, 0, "FE_mesas")
        self.layout.layer( 111, 0, "FE_WF_marks")
        self.layout.layer( 112, 0, "FE_dev_pads")
        self.layout.layer( 113, 0, "FE_dev_texts")
        self.layout.layer( 114, 0, "FE_big_marks")
        self.layout.layer( 115, 0, "FE_big_marks_texts")
        self.layout.layer( 116, 0, "FE_mesa_fields")
        self.layout.layer( 117, 0, "FE_mesa_fields_pads")
        self.layout.layer( 118, 0, "FE_mesa_fields_texts")
        self.layout.layer( 119, 0, "FE_text")
        self.layout.layer( 120, 0, "Islands_p")
        self.layout.layer( 121, 0, "Islands_p_c")
        self.layout.layer( 122, 0, "Islands_p_big")
        self.layout.layer( 123, 0, "Islands_p_big_c")
        self.layout.layer( 130, 0, "LE1_p_small")
        self.layout.layer( 131, 0, "LE1_p_small_c")
        self.layout.layer( 132, 0, "LE1_p_big")
        self.layout.layer( 133, 0, "LE1_p_big_c")
        self.layout.layer( 140, 0, "Bridge_PR")
        self.layout.layer( 150, 0, "LE2_p_small")
        self.layout.layer( 151, 0, "LE2_p_small_c")
        self.layout.layer( 152, 0, "LE2_p_big")
        self.layout.layer( 153, 0, "LE2_p_big_c")
        self.layout.layer( 160, 0, "SiN_mesa")
        self.layout.layer( 161, 0, "SiN_big")
        self.layout.layer( 170, 0, "Shunt_array")
        self.layout.layer( 171, 0, "Shunt")
        self.layout.layer( 180, 0, "TE_small")
        self.layout.layer( 181, 0, "TE_big")

    def init(self):
        self.layout = pya.Layout()
        self.build_layers()
        self.top_cell = self.layout.create_cell( "TOP")
        mask_f.build_WF_marker_cell( self, "FE_WF_marks")
        mask_f.build_Global_marker_cell( self, "FE_big_marks")
        mask_f.wf_marks_coordinates_fun(self)
        mask_f.Global_marks_coordinates_fun(self)

    mask_name = "DS_N5_1"
    # mask_name = "DS_N8_1"
    # mask_name = "DS_N9_1"
    # mask_name = "DS_N12_1"
    # mask_name = "DS_N13_1"

    n_x_devices = 11
    n_y_devices = 11
    x_pitch = 600
    y_pitch = 600

    x_dev_size_sum = x_pitch * (n_x_devices + 1)
    y_dev_size_sum = y_pitch * (n_y_devices + 1)

    WF_size_small = 200

    mesa_off_pads = 50
    mesa_off = 0.5

    pad_off = 5

    meas_areas = np.linspace(0.10, 0.52, 22)
    meas_areas = np.linspace(0.10, 0.1 + 0.02 * (22 - 1), 22)
    meas_areas = np.logspace(np.log10(0.11), np.log10(0.5), 22)
    mesa_under_etch = 0.1

    slot_w = np.array((6,7,8,6,7,8))
    slot_l = np.array((8,8,8,10,10,10))

    # Etching sizes
    island_L = 5
    island_W = 5
    island_ext = 0.5
    small_etching_area_side = 40
    large_etching_area_side = 120
    etch_overlap = 10

    # LE1 sizes
    small_LE_area_side = 40
    LE_pad = 150
    big_LE_area_side = 200
    LE1_overlap = 5

    # bridges
    Bridge_PR_island_x_trim = 0.1
    Bridge_PR_island_width = 1.5

    # LE2 sizes
    mesa_LE2_clearence_x = 3.5
    mesa_LE2_clearence_y = 3
    LE2_overlap = 5

    # WF markers size
    wf_marks_coordinates = []
    WF_marker_pitch = 20
    leg_len = 5
    leg_wid = 0.5
    flap_wid = 2
    flap_len = 2

    # Global markers size
    Global_marks_coordinates = []
    Global_marks_names = []
    Global_marker_pitch = 20
    Global_leg_len = 60
    Global_leg_wid = 5
    Global_marker_corner_pitch = ((n_x_devices+1)*x_pitch) + 400
    Global_marker_pitch = 200
    Global_marker_shift = ((n_x_devices-1)*x_pitch)/2
    Global_mark_off = 40
    Global_mark_off_x = -14
    Global_mark_text_size = 0.00005 # 14
    Gobal_taper_len = 7


    # shunt array
    shunt_array_w = 2
    shunt_array_l = 60
    shunt_array_pitch = 5
    shunt_array_number = 6
    shunt_array_off_beg = 5

    # shut
    g0 = 130e-3
    margin = 1.5
    ito_cond = 4e4 * 1e-6
    ito_thick = 300e-3
    ito_length = 15
    ito_pad = 50

    # SiN open
    mesa_open_margin = 0.1
    SiN_LE_open_size = 140

    # FE
    bridge_1_w = 1
    bridge_2_w = 2
    bridge_2_l = 1

    inner_w = 1

    inner_clearance = 1

    TL_extend = 10
    TL_width = 2

    FE_pad_size = 150

    # mesa fields
    mesa_fields_pitches = np.array((4,5,6,7))
    mesa_fields_areas = meas_areas
    mesa_field_x_pitch = 600
    mesa_field_y_pitch = 7200
    mesa_field_num = int(mesa_fields_areas.size/2)


#################################################################


def build_device( mask_obj, cell_name, slot_w, slot_l, area):

    mask_f.build_mesas( mask_obj, cell_name, slot_w, slot_l, area)
    mask_f.build_WF_markers( mask_obj, cell_name)
    mask_f.build_p_islands( mask_obj, cell_name, slot_w)
    mask_f.build_p_LE_1( mask_obj, cell_name, slot_w, slot_l)
    mask_f.PR_bridges( mask_obj, cell_name, slot_w)
    mask_f.build_p_LE_2( mask_obj, cell_name, slot_w, slot_l)
    mask_f.SiN_opening( mask_obj, cell_name, slot_w, area)
    mask_f.build_shunting( mask_obj, cell_name, slot_l, area)
    mask_f.build_TE( mask_obj, cell_name, slot_w, slot_l, area)

def build_AUX( mask_obj, cell_name):
    mask_f.build_Global_markers( mask_obj, cell_name)
    mask_b.write_text(mask_obj.layout, cell_name, "FE_text", 0.000004, 0, 6800, 0, mask_obj.mask_name)
    mask_f.mesa_fields(mask_obj, cell_name)
    build_pads_mesa_measure(mask_obj, cell_name)

def build_pads_mesa_measure(mask_obj, cell_name):
    for i_column in range(2):
        for i_row in range(11):

            active_cell_name = "T_" + str(i_column) + "_" + str(i_row)
            active_cell = mask_obj.layout.create_cell( active_cell_name)

            mesa_radius_index = (i_row  + i_column * 11)
            area = mask_obj.meas_areas[mesa_radius_index]

            mask_f.build_mesas_pads( mask_obj, active_cell_name, area)
            mask_f.build_pads( mask_obj, active_cell_name)
            mask_f.build_WF_markers( mask_obj, active_cell_name)
            mask_f.SiN_opening_pads( mask_obj, active_cell_name, area)
            mask_f.build_TE_pads(mask_obj, active_cell_name)

            mpa.shift_cell( mask_obj.layout, active_cell_name, i_column * 7200 - 600, i_row * 600)
            mpa.sub_cell_to_TOPcell( mask_obj.layout, mask_obj.top_cell, active_cell_name, 0, 0)


def post_mortem(mask_obj, top_cell):

    top_cell.flatten(1)

    # shift to final
    shiftx = mask_obj.Global_marker_shift - 5000
    shifty = mask_obj.Global_marker_shift - 5000
    trans = pya.Trans.new(int(-shiftx*1000),int(-shifty*1000))
    top_cell.transform(trans)

    path = os.path.join( "..", "gds", "V1", mask_obj.mask_name + ".gds")
    mask_obj.layout.write( path)



#################################################################

def main():
    mask_instance = mask_paramters()
    mask_instance.init()
    generate_lay_file(mask_instance)
    generate_pls_file(mask_instance)

    for row_index in range(mask_instance.n_x_devices):
        for column_index in range(mask_instance.n_y_devices):

            dev_indy = int(row_index/2)
            slot_w = mask_instance.slot_w[dev_indy]
            slot_l = mask_instance.slot_l[dev_indy]

            mesa_radius_index = (row_index * mask_instance.n_y_devices + column_index)%(mask_instance.n_x_devices + mask_instance.n_y_devices)

            active_cell_name = "D_" + str(column_index) + "_" + str(row_index)
            active_cell = mask_instance.layout.create_cell( active_cell_name)
            build_device( mask_instance, active_cell_name, slot_w, slot_l, mask_instance.meas_areas[mesa_radius_index])

            mpa.shift_cell( mask_instance.layout, active_cell_name, column_index * mask_instance.x_pitch, row_index * mask_instance.y_pitch)
            mpa.sub_cell_to_TOPcell( mask_instance.layout, mask_instance.top_cell, active_cell_name, 0, 0)

    build_AUX( mask_instance, mask_instance.top_cell.name)

    post_mortem(mask_instance, mask_instance.top_cell)


if __name__ == "__main__":
    main()
