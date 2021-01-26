def save(results, analyses, configs):

    print('\nSave results? (yes / y , no / n) \n')
    y_n = str(input())
    if y_n == 'no' or y_n == 'n':
        print('Skipping save.')
    elif y_n == 'yes' or y_n == 'y':
        print('\nWhich file formats?(separate by commas):\n\nAvailable File Formats:\n')
        print('   .json:\tjson\n   .js:\t\td3.js\n   .vsp3:\tvsp3\n   .stl:\tstl\n' + \
            '.geo:\tgeo\n   .su2:\tsu2\n   .mm:\t\tmm\n   .dat:\tdat\n   or all:\t all')
        files_to_save = str(input())
        
        vehicle = configs.base
        if 'all' in files_to_save: files_to_save = 'json,d3.js,su2,geo,stl,vsp3,mm,dat'
        if 'json' in files_to_save: save_json(results, vehicle.tag + '.json')   #Save json
        if 'd3.js' in files_to_save: save_d3js(results, vehicle.tag + '.js')    #Save d3js
        if 'su2' in files_to_save:                                              #Save su2
            save_vsp3.write(vehicle,vehicle.tag)
            save_stl(vehicle, vehicle.tag,True,2,True)
            save_geo(vehicle.tag)
            save_su2(vehicle.tag)
        elif 'geo' in files_to_save:                                            #Save geo
            save_vsp3.write(vehicle,vehicle.tag)
            save_stl(vehicle, vehicle.tag,True,2,True)
            save_geo(vehicle.tag)
        elif 'stl' in files_to_save:                                            #Save stl
            save_vsp3.write(vehicle,vehicle.tag)
            save_stl(vehicle, vehicle.tag,True,2,True)
        elif 'vsp3' in files_to_save:
            save_vsp3.write(vehicle,vehicle.tag)                                #Save vsp3
        if 'mm' in files_to_save:   save_mm(results,vehicle.tag + '.mm')        #Save mm
        if 'dat' in files_to_save:                              #Save results in text form
            print_results.print_compress_drag(vehicle,analyses)
            print_results.print_engine_data(vehicle)
            print_results.print_mission_breakdown(results)
            #print_results.print_parasite_drag(ref_conditions, vehicle, analyses)
            print_results.print_weights.print_weight_breakdown(configs.base)

        #If no correct Format is specified:
        if not'json' in files_to_save and 'd3js' in files_to_save and 'vsp3' \
            in files_to_save and 'stl' in files_to_save and 'geo' in files_to_save \
            and 'su2' in files_to_save and 'mm' in files_to_save and 'dat' in files_to_save:
            print('\nERROR: File format not recognized. Try again.')
            return save(results)
        return
    else: 
        print('\n ERROR: Answer not recognized.')
        return save(results)
