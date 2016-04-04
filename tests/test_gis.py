# -*- coding: utf-8 -*-
##
##  test_inflow.py
##  RAPIDpy
##
##  Created by Alan D. Snow.
##  Copyright © 2016 Alan D Snow. All rights reserved.
##

from nose.tools import ok_
import os

#local import
from RAPIDpy.gis.workflow import CreateAllStaticECMWFRAPIDFiles
from RAPIDpy.helper_functions import (compare_csv_decimal_files,
                                      remove_files)
#GLOBAL VARIABLES
MAIN_TESTS_FOLDER = os.path.dirname(os.path.abspath(__file__))
COMPARE_DATA_PATH = os.path.join(MAIN_TESTS_FOLDER, 'compare', 'gis')
INPUT_DATA_PATH = os.path.join(MAIN_TESTS_FOLDER, 'data', 'gis')
OUTPUT_DATA_PATH = os.path.join(MAIN_TESTS_FOLDER, 'output')

#------------------------------------------------------------------------------
# MAIN TEST SCRIPTS
#------------------------------------------------------------------------------
def test_run_era_interim_inflow():
    """
    Checks generating inflow file from ERA Interim LSM
    """
    print "TEST 1: TEST GENERATE INFLOW FILE FROM ERA INTERIM DATA"
    CreateAllStaticECMWFRAPIDFiles(in_drainage_line=os.path.join(INPUT_DATA_PATH, 'flowline.shp'),
                                   river_id="COMID",
                                   length_id="LENGTHKM",
                                   slope_id="Slope",
                                   next_down_river_id="NextDownID",
                                   in_catchment=os.path.join(INPUT_DATA_PATH, 'catchment.shp'),
                                   catchment_river_id="FEATUREID",
                                   rapid_output_folder=OUTPUT_DATA_PATH,
                                   kfac_length_units="km",
                                   )
    
    #CHECK OUTPUT   
    #comid_lat_lon_z
    generated_comid_lat_lon_z_file = os.path.join(OUTPUT_DATA_PATH, 
                                                  "comid_lat_lon_z.csv")
    generated_comid_lat_lon_z_file_solution = os.path.join(COMPARE_DATA_PATH,
                                                           "comid_lat_lon_z.csv")
    ok_(compare_csv_decimal_files(generated_comid_lat_lon_z_file, 
                                  generated_comid_lat_lon_z_file_solution))

    #rapid_connect
    generated_rapid_connect_file = os.path.join(OUTPUT_DATA_PATH, 
                                                  "rapid_connect.csv")
    generated_rapid_connect_file_solution = os.path.join(COMPARE_DATA_PATH,
                                                           "rapid_connect.csv")
    ok_(compare_csv_decimal_files(generated_rapid_connect_file, 
                                  generated_rapid_connect_file_solution))

    #riv_bas_id
    generated_riv_bas_id_file = os.path.join(OUTPUT_DATA_PATH, 
                                             "riv_bas_id.csv")
    generated_riv_bas_id_file_solution = os.path.join(COMPARE_DATA_PATH,
                                                      "riv_bas_id.csv")
    ok_(compare_csv_decimal_files(generated_riv_bas_id_file, 
                                  generated_riv_bas_id_file_solution))

    #kfac
    generated_kfac_file = os.path.join(OUTPUT_DATA_PATH, 
                                       "kfac.csv")
    generated_kfac_file_solution = os.path.join(COMPARE_DATA_PATH,
                                                "kfac.csv")
    ok_(compare_csv_decimal_files(generated_kfac_file, 
                                  generated_kfac_file_solution))
    
    #k
    generated_k_file = os.path.join(OUTPUT_DATA_PATH, 
                                    "k.csv")
    generated_k_file_solution = os.path.join(COMPARE_DATA_PATH,
                                             "k.csv")
    ok_(compare_csv_decimal_files(generated_k_file, 
                                  generated_k_file_solution))

    #x
    generated_x_file = os.path.join(OUTPUT_DATA_PATH, 
                                    "x.csv")
    generated_x_file_solution = os.path.join(COMPARE_DATA_PATH,
                                             "x.csv")
    ok_(compare_csv_decimal_files(generated_x_file, 
                                  generated_x_file_solution))

    #weight_ecmwf_t1279
    generated_weight_ecmwf_t1279_file = os.path.join(OUTPUT_DATA_PATH, 
                                                     "weight_ecmwf_t1279.csv")
    generated_weight_ecmwf_t1279_file_solution = os.path.join(COMPARE_DATA_PATH,
                                                              "weight_ecmwf_t1279.csv")
    ok_(compare_csv_decimal_files(generated_weight_ecmwf_t1279_file, 
                                  generated_weight_ecmwf_t1279_file_solution))

    #weight_ecmwf_tco369
    generated_weight_ecmwf_tco369_file = os.path.join(OUTPUT_DATA_PATH, 
                                                     "weight_ecmwf_tco369.csv")
    generated_weight_ecmwf_tco369_file_solution = os.path.join(COMPARE_DATA_PATH,
                                                              "weight_ecmwf_tco369.csv")
    ok_(compare_csv_decimal_files(generated_weight_ecmwf_tco369_file, 
                                  generated_weight_ecmwf_tco369_file_solution))

    #weight_era_t511
    generated_weight_era_t511_file = os.path.join(OUTPUT_DATA_PATH, 
                                                     "weight_era_t511.csv")
    generated_weight_era_t511_file_solution = os.path.join(COMPARE_DATA_PATH,
                                                              "weight_era_t511.csv")
    ok_(compare_csv_decimal_files(generated_weight_era_t511_file, 
                                  generated_weight_era_t511_file_solution))

    remove_files(generated_comid_lat_lon_z_file,
                 generated_rapid_connect_file,
                 generated_riv_bas_id_file,
                 generated_kfac_file,
                 generated_k_file,
                 generated_x_file,
                 generated_weight_ecmwf_t1279_file,
                 generated_weight_ecmwf_tco369_file,
                 generated_weight_era_t511_file)

if __name__ == '__main__':
    import nose
    nose.main()