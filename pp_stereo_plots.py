
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import gridspec
import mplstereonet
import os, glob
import shutil


pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1500)

stereo_files_path   = '/Users/sfranke/Seafile/Orca/2019_EGRIP_Field/PP_Results/stereo_plots/stereo_plot_files/'
#figure_path         = '/Users/sfranke/Seafile/Orca/2019_EGRIP_Field/PP_Results/stereo_plots/stereo_plots_rotated/'

os.chdir(stereo_files_path)


#cmap='ocean_r'
cmap='Blues'


#%%

#############
# 
#############

if 0:
    
    stereo_list = []
    
    for file in glob.glob('stereo_EGRIP3???*_*_20.txt'):
        if 'vertical' not in file:
            if 'volume' not in file:
                if 'horizontal' not in file:
                    file_ = file.split('_EGRIP')[1].split('_')[0] + '_' + file.split('_')[2]
                    print("['" + file_ + "', " + "],")



#%%



if 0:
    Folder_List = []
    for file in glob.glob('*.txt'):
        folder = file.split('_')[1].split('EGRIP')[1] + '_'
        Folder_List.append(folder)
        
    Folder_List = set(Folder_List)
    
    for folder in Folder_List:
        if not os.path.exists('EGRIP_' + folder.split('_')[0]):
            os.mkdir('EGRIP_' + folder.split('_')[0])
            for stereo in glob.glob('stereo_EGRIP' + folder + '*_*.txt'):
                shutil.copy(stereo, 'EGRIP_' + folder.split('_')[0])


#%%

#############################################################
# Single Plots ===>>  ROTATED or UNROTATED
# doing a plot for every file in the stero_path_folder *.txt
# or from a list with rotation values
#############################################################

if 0:
    
    do_the_rotation = False
    
    
    if do_the_rotation == True:
        
        # save output figures here
        figure_path = '/Users/sfranke/Seafile/Orca/2019_EGRIP_Field/PP_Results/stereo_plots/stereo_plots_rotated/'
        
        # load rotation data from file
        df_rotation = pd.read_csv('/Users/sfranke/Seafile/Orca/2019_EGRIP_Field/PP_Results/stereo_plots/rotation_list.csv', delimiter='\t')
        
        print('')
        print('++++ Plotting rotated Stereo Plots and Rose Diagrams')
        print('++++ Figure Path: {}'.format(figure_path))
        print('')
        
        for i in range(len(df_rotation)):
            
            rotation_bag_section    = str(df_rotation['bag_section'][i])
            rotation                = int(df_rotation['rotation'][i])
            
            file = 'stereo_EGRIP' + rotation_bag_section + '_20.txt'
            
    
            # Reading Data and defining variables
            df                  = pd.read_csv(file, delimiter='\t')
            df.columns          = ['azimuth', 'latitude']
            azimuth, latitude   = df['azimuth'], df['latitude']
            azimuth             = azimuth + rotation
            number_of_grains    = str(df.shape[0])
            appendix            = ''
            
    
            # Determining Bagnumber and section type via the filename
            # 1. Going for regular files (no volume sections)
            try:
                if 1:
                    Bag         = file.split('_')[1].split('EGRIP')[1]
                    Segment     = file.split('_')[2]
                    Filename    = 'EGRIP' + '_' + Bag + '_' + Segment + appendix
                    Depth       = ((float(Bag) * 0.55) + (float(Segment)) * (0.55/6)) - 0.55
                    Depth_p     = np.round(Depth, decimals=1).astype(str)
                
                if 0:
                    Bag         = file.split('_')[3]
                    Segment     = file.split('_')[4]
                    Filename    = 'S5' + '_' + Bag + '_' + Segment + appendix
                    Depth       = ((float(Bag) * 0.55) + (float(Segment)) * (0.55/6)) - 0.55
                    Depth_p     = np.round(Depth, decimals=1).astype(str)
                
            except ValueError:
                pass
            
            '''
            try:
                if 0:
                    # 2. Going for horizontal volume samples
                    if 'horizontal' in file:
                        Bag         = file.split('_')[1].split('EGRIP')[1]
                        Segment     = file.split('_')[4]
                        Filename    = 'EGRIP' + '_' + Bag + '_Volume_Horizontal_' + Segment + appendix
                        Depth       = (float(Bag) * 0.55) - 0.55
                        Depth_p     = np.round(Depth, decimals=1).astype(str)
                    
                    # 3. Going for vertical volume samples
                    elif 'vertical' in file:
                
                        Bag         = file.split('_')[1].split('EGRIP')[1]
                        Segment     = file.split('_')[4]
                        Filename    = 'EGRIP' + '_' + Bag + '_Volume_Vertical_' + Segment + appendix
                        Depth       = (float(Bag) * 0.55) - 0.55
                        Depth_p     = np.round(Depth, decimals=1).astype(str)
                        
                if 1:
                    # 2. Going for horizontal volume samples
                    if 'horizontal' in file:
                        Bag         = file.split('_')[3]
                        Segment     = file.split('_')[6]
                        Filename    = 'S5' + '_' + Bag + '_Volume_Horizontal_' + Segment + appendix
                        Depth       = (float(Bag) * 0.55) - 0.55
                        Depth_p     = np.round(Depth, decimals=1).astype(str)
                    
                    # 3. Going for vertical volume samples
                    elif 'vertical' in file:
                
                        Bag         = file.split('_')[3]
                        Segment     = file.split('_')[4]
                        Filename    = 'S5' + '_' + Bag + '_Volume_Vertical_' + Segment + appendix
                        Depth       = (float(Bag) * 0.55) - 0.55
                        Depth_p     = np.round(Depth, decimals=1).astype(str)
                    
            except:
                # if none of the filename criteria are fullfilled, 
                # I'll trow an error and pass
                print('===> !!!! An Error occured while reading the filename ...')
                print('===> Skipping....')
                print('')
                pass
           
            '''
            
            # 
            bin_edges                       = np.arange(0, 365, 10)
            number_of_strikes, bin_edges    = np.histogram(azimuth, bin_edges)
            bin_data                        = number_of_strikes
            
            
            ###############
            #   Plotting  #
            ###############
        
            print('===> Plotting: {}'.format(Filename))
            
            fig = plt.figure(figsize=(16,18.5))
            ax  = fig.add_subplot(121, projection='stereonet')
            #plt.suptitlle()
            
            ax.pole(azimuth -90, latitude -90, c='k', label='Pole of the Planes', \
                    markersize=1.75, alpha=0.5)
            dens = ax.density_contourf(azimuth -90, latitude -90, measurement='poles', \
                                       cmap=cmap, levels=15)
            #ax.set_title(Filename + '\nDepth: ' + Depth_p + ' m' + \
                         #'\n Number of Grains: ' + '{:04d}'.format(int(number_of_grains)),\
                         #y=1.15, fontsize=20)
            #ax.set_title('Depth: {} m\nBag: {}\nNumber of Grains: {}'.format(\
            #            Depth_p, Filename, int(number_of_grains)), y=1.10, fontsize=20)
            
            ax.set_title('Depth: {} m'.format(\
                         Depth_p), y=1.15, fontsize=28)
            ax.grid()
            #cbaxes = fig.add_axes([0.54, 0.375, 0.02, 0.25]) 
            #fig.colorbar(dens, orientation='vertical', cax=cbaxes, label='Density', format='%.1f')
        
            if 1:
                ax2 = fig.add_subplot(122, projection='polar')
        
                ax2.bar(np.deg2rad(np.arange(0, 360, 10)), bin_data, 
                       width=np.deg2rad(10), bottom=0.0, color='.8', edgecolor='k')
                ax2.set_theta_zero_location('N')
                ax2.set_theta_direction(-1)
                ax2.set_thetagrids(np.arange(0, 360, 10), labels=np.arange(0, 360, 10))
                #ax2.set_rgrids(np.arange(1, two_halves.max() + 1, 2), angle=0, weight= 'black')
                #ax2.set_title('Rose Diagram of the "Fault System"', y=1.10, fontsize=20)
                ax2.set_title('Bag: {}_{}'.format(Bag, Segment), y=1.15, fontsize=28)
            
            plt.savefig(figure_path + 'Stereo_rotated_' + Filename + '.png', \
                        dpi=200, bbox_inches='tight') 
            print('===> Saved: Stereo_rotated_{}.png'.format(Filename))
            print('')
            plt.close()
    
    
    ############################
    ############################
    
    if do_the_rotation == False:
        
        figure_path = '/Users/sfranke/Seafile/Orca/2019_EGRIP_Field/PP_Results/stereo_plots/stereo_plot_plots_single/'
        
        print('')
        print('++++ Plotting not-rotated Stereo Plots and Rose Diagrams')
        print('++++ Figure Path: {}'.format(figure_path))
        print('')
        
        for file in sorted(glob.glob('*.txt')):
            
            rotation = 0
            
            # Reading Data and defining variables
            df                  = pd.read_csv(file, delimiter='\t')
            df.columns          = ['azimuth', 'latitude']
            azimuth, latitude   = df['azimuth'], df['latitude']
            azimuth             = azimuth + rotation
            number_of_grains    = str(df.shape[0])
            appendix            = ''
            
    
            # Determining Bagnumber and section type via the filename
            # 1. Going for regular files (no volume sections)
            try:
                if 1:
                    Bag         = file.split('_')[1].split('EGRIP')[1]
                    Segment     = file.split('_')[2]
                    Filename    = 'EGRIP' + '_' + Bag + '_' + Segment + appendix
                    Depth       = ((float(Bag) * 0.55) + (float(Segment)) * (0.55/6)) - 0.55
                    Depth_p     = np.round(Depth, decimals=1).astype(str)
                
                if 0:
                    Bag         = file.split('_')[3]
                    Segment     = file.split('_')[4]
                    Filename    = 'S5' + '_' + Bag + '_' + Segment + appendix
                    Depth       = ((float(Bag) * 0.55) + (float(Segment)) * (0.55/6)) - 0.55
                    Depth_p     = np.round(Depth, decimals=1).astype(str)
                
            except ValueError:
                pass
            
           
            try:
                if 0:
                    # 2. Going for horizontal volume samples
                    if 'horizontal' in file:
                        Bag         = file.split('_')[1].split('EGRIP')[1]
                        Segment     = file.split('_')[4]
                        Filename    = 'EGRIP' + '_' + Bag + '_Volume_Horizontal_' + Segment + appendix
                        Depth       = (float(Bag) * 0.55) - 0.55
                        Depth_p     = np.round(Depth, decimals=1).astype(str)
                    
                    # 3. Going for vertical volume samples
                    elif 'vertical' in file:
                
                        Bag         = file.split('_')[1].split('EGRIP')[1]
                        Segment     = file.split('_')[4]
                        Filename    = 'EGRIP' + '_' + Bag + '_Volume_Vertical_' + Segment + appendix
                        Depth       = (float(Bag) * 0.55) - 0.55
                        Depth_p     = np.round(Depth, decimals=1).astype(str)
                        
                if 1:
                    # 2. Going for horizontal volume samples
                    if 'horizontal' in file:
                        Bag         = file.split('_')[3]
                        Segment     = file.split('_')[6]
                        Filename    = 'S5' + '_' + Bag + '_Volume_Horizontal_' + Segment + appendix
                        Depth       = (float(Bag) * 0.55) - 0.55
                        Depth_p     = np.round(Depth, decimals=1).astype(str)
                    
                    # 3. Going for vertical volume samples
                    elif 'vertical' in file:
                
                        Bag         = file.split('_')[3]
                        Segment     = file.split('_')[4]
                        Filename    = 'S5' + '_' + Bag + '_Volume_Vertical_' + Segment + appendix
                        Depth       = (float(Bag) * 0.55) - 0.55
                        Depth_p     = np.round(Depth, decimals=1).astype(str)
                    
            except:
                # if none of the filename criteria are fullfilled, 
                # I'll trow an error and pass
                print('===> !!!! An Error occured while reading the filename ...')
                print('===> Skipping....')
                print('')
                pass
           
            
            
            # Rose Diagram params
            bin_edges                       = np.arange(0, 365, 10)
            number_of_strikes, bin_edges    = np.histogram(azimuth, bin_edges)
            bin_data                        = number_of_strikes
            
            
            ###############
            #   Plotting  #
            ###############
        
            print('===> Plotting: {}'.format(Filename))
            
            fig = plt.figure(figsize=(16,18.5))
            ax  = fig.add_subplot(121, projection='stereonet')
            #plt.suptitlle()
            
            ax.pole(azimuth -90, latitude -90, c='k', label='Pole of the Planes', \
                    markersize=1.75, alpha=0.5)
            dens = ax.density_contourf(azimuth -90, latitude -90, measurement='poles', \
                                       cmap=cmap, levels=15)
            #ax.set_title(Filename + '\nDepth: ' + Depth_p + ' m' + \
                         #'\n Number of Grains: ' + '{:04d}'.format(int(number_of_grains)),\
                         #y=1.15, fontsize=20)
            #ax.set_title('Depth: {} m\nBag: {}\nNumber of Grains: {}'.format(\
            #            Depth_p, Filename, int(number_of_grains)), y=1.10, fontsize=20)
            
            ax.set_title('Depth: {} m'.format(\
                         Depth_p), y=1.15, fontsize=28)
            ax.grid()
            #cbaxes = fig.add_axes([0.54, 0.375, 0.02, 0.25]) 
            #fig.colorbar(dens, orientation='vertical', cax=cbaxes, label='Density', format='%.1f')
        
            if 1:
                ax2 = fig.add_subplot(122, projection='polar')
        
                ax2.bar(np.deg2rad(np.arange(0, 360, 10)), bin_data, 
                       width=np.deg2rad(10), bottom=0.0, color='.8', edgecolor='k')
                ax2.set_theta_zero_location('N')
                ax2.set_theta_direction(-1)
                ax2.set_thetagrids(np.arange(0, 360, 10), labels=np.arange(0, 360, 10))
                #ax2.set_rgrids(np.arange(1, two_halves.max() + 1, 2), angle=0, weight= 'black')
                #ax2.set_title('Rose Diagram of the "Fault System"', y=1.10, fontsize=20)
                ax2.set_title('Bag: {}_{}'.format(Bag, Segment), y=1.15, fontsize=28)
            
            plt.savefig(figure_path + 'Stereo_' + Filename + '.png', \
                        dpi=200, bbox_inches='tight') 
            print('===> Saved: Stereo_{}.png'.format(Filename))
            print('')
            plt.close()


#%%
        
#############################################################
# Bag Plots
# doing a plot for every file in the stero_path_folder *.txt
#############################################################


if 0:
    
    figure_path         = '/Users/sfranke/Seafile/Orca/2019_EGRIP_Field/PP_Results/stereo_plots/stereo_files_S5_ShearMargin/'
    
    for folder in Folder_List:
        os.chdir(stereo_files_path + 'EGRIP_' + str(folder.split('_')[0]))
        
        fig = plt.figure(figsize=(45,7.5))
        fig.subplots_adjust(hspace=0.4, wspace=0.4)
        for i in range (1, 7):
            try:
                file = glob.glob('*.txt')[i - 1]

                    
                # Reading Data and defining variables
                df                  = pd.read_csv(file, delimiter='\t')
                df.columns          = ['azimuth', 'latitude']
                azimuth, latitude   = df['azimuth'], df['latitude']
                number_of_grains    = str(df.shape[0])
                appendix            = ''
                
         
                # Determining Bagnumber and section type via the filename
                # 1. Going for regular files (no volume sections)
                try:
                    Bag         = file.split('_')[1].split('EGRIP')[1]
                    Segment     = file.split('_')[2]
                    Filename    = 'EGRIP' + '_' + Bag + '_' + Segment
                    Depth       = ((float(Bag) * 0.55) + (float(Segment)) * (0.55/6)) - 0.55
                    Depth_p     = np.round(Depth, decimals=1).astype(str)
                    
                except ValueError:
                    pass
                
                try:
                    # 2. Going for horizontal volume samples
                    if 'horizontal' in file:
                        Bag         = file.split('_')[1].split('EGRIP')[1]
                        Segment     = file.split('_')[4].split('.')[0]
                        Filename    = 'EGRIP' + '_' + Bag + '_Volume_Horizontal_' + Segment
                        Depth       = (float(Bag) * 0.55) - 0.55
                        Depth_p     = np.round(Depth, decimals=1).astype(str)
                    
                    # 3. Going for vertical volume samples
                    elif 'vertical' in file:
                
                        Bag         = file.split('_')[1].split('EGRIP')[1]
                        Segment     = file.split('_')[4].split('.')[0]
                        Filename    = 'EGRIP' + '_' + Bag + '_Volume_Vertical_' + Segment
                        Depth       = (float(Bag) * 0.55) - 0.55
                        Depth_p     = np.round(Depth, decimals=1).astype(str)
                        
                except:
                    # if none of the filename criteria are fullfilled, 
                    # I'll trow an error and pass
                    print('===> !!!! An Error occured while reading the filename ...')
                    print('File: {}'.format(file))
                    pass
                                        
                

                print('===> Plotting: {}'.format(Filename))
                
                #ax = 'ax' + str(num)
                axs = fig.add_subplot(1, 6, i, projection='stereonet')
                
                
                axs.pole(azimuth -90, latitude -90, c='k', label='Pole of the Planes', \
                        markersize=1.5, alpha=0.5)
                dens = axs.density_contourf(azimuth -90, latitude -90, \
                                           measurement='poles', cmap=cmap)
                #ax.set_title(Filename + '\nDepth: ' + Depth_p + ' m' + \
                             #'\n Number of Grains: ' + '{:04d}'.format(int(number_of_grains)),\
                             #y=1.15, fontsize=20)
                axs.set_title('Depth: {} m\nBag: {}\nNumber of Grains: {}'.format(\
                             Depth_p, Filename, int(number_of_grains)), y=1.10, fontsize=22)
                axs.grid()
                #cbaxes = fig.add_axes([0.54, 0.375, 0.02, 0.25]) 
                #plt.colorbar(dens, orientation='vertical', cax=cbaxes, label='Density', format='%.1f')
            
            except IndexError:
                pass
            
        plt.savefig(figure_path + 'Stereos_' + 'EGRIP_' + str(folder.split('_')[0]) + '.png', \
                    dpi=300, bbox_inches='tight') 
        print('===> Saved: {}'.format(Filename))
        print('')
        plt.close()   


#%%
    
#############################################################
# Radargram + Plots for Timelapse
# doing a plot for every file in the stero_path_folder *.txt
#############################################################
    
if 1:
    
    import geopy.distance
    
    #rotation_list = [['3746_1', 90]]
    
    figure_path = '/Users/sfranke/Seafile/Orca/2019_EGRIP_Field/PP_Results/stereo_plots/stereo_plots_rotated_withRadargram/'

    path = '/Users/sfranke/Seafile/Orca/2019_EGRIP_Field/PP_Results/stereo_plots/radar_profile_egrip/'
    data = 'Data_20180510_01_002_elevation.csv'
    meta =  'Data_20180510_01_002_meta_v2.csv'
    
    
    dfr   = pd.read_csv(path + data)
    meta  = pd.read_csv(path + meta)
    
    cmp = np.array(range(1, len(dfr.columns) + 1))
    
    core_depth = np.arange(0, dfr.index.shape[0]) - 35
    avy_max = dfr.index.shape[0]/(dfr.index.shape[0] - 35) - 1
    avy_min = (dfr.index.shape[0] /(3856 * 0.55)) - 1
    
    
    elevation = np.array(dfr['ElevationWGS84'])
    del dfr['ElevationWGS84']
    
    
    # set number of ticks on x axis
    number_of_xticks = 50
    step = np.round(dfr.shape[1] / number_of_xticks).astype(int)
    
    # Here we define our x-axis distance
    # (1) We take our lat/lon info to calculate distance from point to point,
    # (2) then we sum sum everything up (cumsum) to get our distance array
    # (3) Then we set our spacing for the y axis in meters
    
    spacing_k = np.array(0)
    spacing_m = np.array(0)
    
    # (1)
    for i in range(1, len(meta)-1):
    	coord_1 = (meta['Lat'][i], meta['Lon'][i])
    	coord_2 = (meta['Lat'][i + 1], meta['Lon'][i + 1])
    	fk = geopy.distance.geodesic(coord_1, coord_2).kilometers
    	spacing_k = np.append(spacing_k, fk)
	    
    distance_k = np.around(np.cumsum(spacing_k[0:-1]), 0)
    distance_k = distance_k.astype(int)
    distance_k2 = np.around(np.cumsum(spacing_k[0:-1]), 2)
    
    
    # (2)
    for i in range(1, len(meta)-1):
    	coord_1 = (meta['Lat'][i], meta['Lon'][i])
    	coord_2 = (meta['Lat'][i + 1], meta['Lon'][i + 1])
    	fm = geopy.distance.geodesic(coord_1, coord_2).meters
    	spacing_m = np.append(spacing_m, fm)    
    
    distance_m = np.around(np.cumsum(spacing_m[0:-1]), 0)

    # (3) 
    y_spacing  = 100
    y_spacing_ = 100
    offset  = np.min([y for y in elevation[0::y_spacing] if y > 0])
    offset_ = np.min([y for y in elevation[0::y_spacing_] if y > 0])
    
    EGRIP = 799
    x_step = 133
    
    
    ##########################################
    # PP Data for Eigenvalues and Grainsize
    ##########################################
    
    pp_path = '/Users/sfranke/Seafile/Orca/2019_EGRIP_Field/PP_Results/PP_Files/'
    pp_file = 'PP_Results_2017-19.csv'
    pp_data = pp_path + pp_file
    
    dfp = pd.read_csv(pp_data, delimiter='\t')
    
    dfp = dfp.sort_values(by=['bag_number', 'bag_section'])
    dfp = dfp.reset_index()
    
    dfp['bagsec'] = dfp['bag_number'].astype(str) + '_' + dfp['bag_section'].astype(str)
    
    e1          = dfp['eigenvalue_e1']
    e2          = dfp['eigenvalue_e2']
    e3          = dfp['eigenvalue_e3']
    grain_size  = dfp['grain_area_mm2']
    depth_pp    = dfp['depth']
    
    
    ###########################
    # Rotation Data from list
    ###########################
    
    df_rotation = pd.read_csv('/Users/sfranke/Seafile/Orca/2019_EGRIP_Field/PP_Results/stereo_plots/rotation_list.csv', delimiter='\t')
        
    
    ############
    # Plotting 
    ############
    
    figure_path = '/Users/sfranke/Seafile/Orca/2019_EGRIP_Field/PP_Results/stereo_plots/stereo_plots_rotated_withRadargram/'

    for i in range(len(df_rotation)):
            
        rotation_bag_section    = str(df_rotation['bag_section'][i])
        rotation                = int(df_rotation['rotation'][i])
        
        file = 'stereo_EGRIP' + rotation_bag_section + '_20.txt'
        
        # Reading Data and defining variables for stereo data
        df                  = pd.read_csv(file, delimiter='\t')
        df.columns          = ['azimuth', 'latitude']
        azimuth, latitude   = df['azimuth'], df['latitude']
        azimuth             = azimuth + rotation
        number_of_grains    = str(df.shape[0])
        appendix            = ''
        
        # retrieve the index of the current stereo file
        # in the PP DATA
        critical = False
        
        try:
            idx = dfp.loc[dfp['bagsec']==rotation_list[i][0]].index[0]
            #idx = id_[0]
        except IndexError:
            critical = True
        
        
        # Determining Bagnumber and section type via the filename
        # 1. Going for regular files (no volume sections)
        try:
            if 1:
                Bag         = file.split('_')[1].split('EGRIP')[1]
                Segment     = file.split('_')[2]
                Filename    = 'EGRIP' + '_' + Bag + '_' + Segment + appendix
                Depth       = ((float(Bag) * 0.55) + (float(Segment)) * (0.55/6)) - 0.55
                Depth_p     = np.round(Depth, decimals=1).astype(str)
            
            if 0:
                Bag         = file.split('_')[3]
                Segment     = file.split('_')[4]
                Filename    = 'S5' + '_' + Bag + '_' + Segment + appendix
                Depth       = ((float(Bag) * 0.55) + (float(Segment)) * (0.55/6)) - 0.55
                Depth_p     = np.round(Depth, decimals=1).astype(str)
            
        except ValueError:
            pass
    
        drill_depth = float(35) + float(Depth_p)

    
        if critical == False:
            
            ################
            #   PLOTTING
            ################
            
            fig = plt.figure(figsize=(20,10))
            gs = gridspec.GridSpec(1, 5,
                           width_ratios=[5, 1, 1, 2, 4],
                           height_ratios=[1]
                           )
            
            plt.suptitle('PP EGRIP Ice Core Tour', fontsize=24)
            
            ## Radargram BIG
            ax1 = fig.add_subplot(gs[0])
            ax1.imshow(dfr, cmap='bone_r', aspect="auto", vmin=-18, vmax=-4, zorder=1)
            
            ax1.set_ylim(3000, 0)
            plt.yticks(np.array(dfr.index)[offset::100], elevation[offset::100])
            plt.xticks(np.array(range(1, len(distance_k), x_step)), distance_k[0::x_step])#['250', '200', '150', '100', '50', '0'])
            plt.ylim(3000, 0)
            plt.xlim(0, 2000)
            plt.xlabel('Distance [km]')
            plt.axvline(x=EGRIP, ymin=0.99, ymax=0.28, color='white', \
                        label='EGRIP Drill Site', linewidth=3, zorder=2)
            plt.axhline(y=drill_depth, linewidth=1, zorder=2)
            drill_head = ax1.scatter(799, drill_depth, s=150, marker='v',\
                                     facecolors='black', edgecolors='black', zorder=3)
            plt.legend()
            plt.ylabel('Elevation a.s.l. [m]')
            plt.title('AWI UWB Profile 180-210 MHz - 2018-05-10')
            
            
            ## Radargram SECTION
            ax2 = fig.add_subplot(gs[1])
            ax2.imshow(dfr, cmap='bone_r', aspect="auto", vmin=-18, vmax=-4, zorder=1)
            
            #ax2.plot(cmp, als, linewidth=5, color='white')
            ax2.set_ylim(3000, 0)
            #plt.yticks(np.array(dfr.index)[offset::100], elevation[offset::100])
            plt.yticks(np.array(dfr.index)[35::100], core_depth[35::100])
            plt.xticks(np.array(range(1, len(distance_k2), 20)), distance_k2[0::20])#['250', '200', '150', '100', '50', '0'])
            plt.ylim(3000, 0)
            plt.xlim(780, 820)
            plt.xlabel('Distance [km]')
            plt.axvline(x=EGRIP, ymin=0.99, ymax=0.28, color='white', \
                        label='EGRIP Drill Site', linewidth=3, zorder=2)
            plt.axhline(y=drill_depth, linewidth=1, zorder=2)
            drill_head = ax2.scatter(799, drill_depth, s=150, marker='v',\
                                     facecolors='black', edgecolors='black', zorder=3)
            #plt.legend()
            #plt.ylabel('')
            plt.title('Core Depth')
    
    
            # Grain Size
            ax3 = fig.add_subplot(gs[2])
            ax3.scatter(grain_size[0:idx], depth_pp[0:idx] + 30, s=grain_size * 3, facecolors='none', \
                        edgecolors='black', label='Mean Grain Area (mm2)', alpha=0.5)
            
            plt.axhline(y=drill_depth, linewidth=1, zorder=2)
            
            plt.yticks(np.array(dfr.index)[35::100], core_depth[35::100])
            plt.ylim(0, 3000)
            plt.xlim(0, grain_size.max() + 2)
            plt.xticks([0, 5, 10])
            plt.xlabel('Area mm^2')
            plt.gca().invert_yaxis()
            plt.grid()
            plt.title('Grainsize')
            
            
            # Eigenvalues
            ax4 = fig.add_subplot(gs[3])
            
            ax4.plot(e1[0:idx], depth_pp[0:idx] + 30, '^', color='blue',\
                        label='e1', markersize=4, alpha=0.4)
            ax4.plot(e2[0:idx], depth_pp[0:idx] + 30, '<', color='purple',\
                        label='e2', markersize=4, alpha=0.4)
            ax4.plot(e3[0:idx], depth_pp[0:idx] + 30, '>', color='orange',\
                        label='e3', markersize=4, alpha=0.4)
            
            plt.axhline(y=drill_depth, linewidth=1, zorder=2)
            plt.yticks(np.array(dfr.index)[35::100], core_depth[35::100])

            plt.xlim(-0.05, 0.9)
            plt.ylim(0, 3000)
            plt.gca().invert_yaxis()
            plt.grid()
            plt.title('Eigenvalues')
    
    
            ax5 = fig.add_subplot(gs[4], projection='stereonet')                
            ax5.pole(azimuth -90, latitude -90, c='k', label='Pole of the Planes', \
                    markersize=1.75, alpha=0.5)
            dens = ax5.density_contourf(azimuth -90, latitude -90, measurement='poles', \
                                       cmap=cmap, levels=15)
            #ax.set_title(Filename + '\nDepth: ' + Depth_p + ' m' + \
                         #'\n Number of Grains: ' + '{:04d}'.format(int(number_of_grains)),\
                         #y=1.15, fontsize=20)
            #ax.set_title('Depth: {} m\nBag: {}\nNumber of Grains: {}'.format(\
            #            Depth_p, Filename, int(number_of_grains)), y=1.10, fontsize=20)
            ax5.set_title('Depth: {} m'.format(\
                         Depth_p), y=1.15, fontsize=28)
            ax5.grid()
            #cbaxes = fig.add_axes([0.54, 0.375, 0.02, 0.25]) 
            #plt.colorbar(dens, orientation='horizontal', label='Grain Density', format='%.1f')
            
            
            ##############
            # SAVE FIGURE
            ##############
            plt.savefig(figure_path + 'Stereo_rotated_withRadargram' + Filename + '.png', \
                        dpi=150)#, bbox_inches='tight') 
            print('===> Saved: Stereo_rotated_with_Radargram_{}'.format(Filename))
            print('')
            plt.close()
        
        if critical == True:
            pass
        
     

