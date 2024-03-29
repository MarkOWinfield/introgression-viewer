# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:39:59 2022

@author: bzmow
"""
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import altair as alt

st.set_page_config(layout="wide")

st.markdown(""" <style> .font1 {
    font-size: 45px; font-family: 'Copper Black'; color: #FF9633}
    </style> """, unsafe_allow_html=True)

st.markdown(""" <style> .font2 {
    font-size: 30px; font-family: 'Copper Black'; color: #FF9633}
    </style> """, unsafe_allow_html=True)


################################# FUNCTIONS ###################################


def getData(filePath):
    df = pd.read_csv(filePath)
     
    return df


def change_index(df):
    bin_list = list(range(1,(len(df) + 1)))
    df['Adjusted Bin'] = bin_list
    # df.set_index('Adjusted Bin', inplace=True)
    
    return df


def changeColNames(dfChrNew):
    
    dfChrNew = dfChrNew.rename(columns={'ENT336': 'Ae. tauschii (ENT336)',
                'BW_01011': 'Ae. tauschii (BW_01011)',
                'BW_01022': 'Ae. tauschii (BW_01022)',
                'BW_01014': 'Ae. tauschii (BW_01014)',
                'BW_01024': 'Ae. tauschii (BW_01024)',
                'BW_01026': 'Ae. tauschii (BW_01026)',
                'BW_01028': 'Ae. tauschii (BW_01028)',
                'dicoccoides-10x_nuq': 'T. dicoccoides',
                'elongathum-10x_nuq': 'Th. elongatum',
                'Lo7_nuq': 'Secale cereale',
                'ponticumG37_nuq': 'Th. ponticum (37)',
                'ponticumG38_nuq': 'Th. ponticum (38)',
                'ponticumG39-10x_nuq': 'Th. ponticum (39)',
                'speltoides-10x_nuq': 'Ae. speltoides',
                'svevo-10x_nuq': 'T. durum (Svevo)',
                'timopheevi10827-10x_nuq': 'T. timopheevii (10827)',
                'timopheevi33255-10x_nuq': 'T. timopheevii (33255)',
                'timopheevii10558_nuq.jf': 'T. timopheevii (10558)',
                'timopheevii10827-10x-all_all': 'T. timopheevii (10827_all)',
                'timopheevii14352_nuq.jf': 'T. timopheevii (14352)',
                'timopheevii15832_nuq.jf': 'T. timopheevii (15832)',
                'timopheevii17024-10x_all': 'T. timopheevii (17024)',
                'timopheevii22438_nuq.jf': 'T. timopheevii (22438)',
                'timopheevii3708_nuq.jf': 'T. timopheevii (3708)',
                'urartu-10x_nuq': 'T. urartu',
                'ventricosa-10x_nuq': 'Ae. ventricosa',
                'ventricosa2067-10x_nuq': 'Ae. ventricosa (2067)',
                'ventricosa2181': 'Ae. ventricosa (2181)',
                'ventricosa2181-10x_nuq': 'Ae. ventricosa (2181 10x)',
                'ventricosa2210-10x_all': 'Ae. ventricosa (2210)',
                'ventricosa2211-10x_nuq': 'Ae. ventricosa (2211)',
                'ventricosa2234-10x_all': 'Ae. ventricosa (2234)',
                'arina-pg': 'Arina',
                'chinese-pg': 'Chinese Spring',
                'jagger-pg': 'Jagger',
                'julius-pg': 'Julius',
                'lancer-pg': 'Lancer',
                'landmark-pg': 'Landmark',
                'mace-pg': 'Mace',
                'mattis-pg': 'Mattis',
                'norin61-pg': 'Norin 61',
                'spelt-pg': 'Spelt',
                'stanley-pg': 'Stanley'
                })
    
    return(dfChrNew)
    

###############################################################################

# for key in st.session_state.keys():
#     del st.session_state[key]

with st.sidebar:
    
    with st.form('my_form', clear_on_submit=False):
    
        refGenome = st.selectbox(
            label='Select Reference Genome:',
            options=('Arina', 'Chinese Spring', 'Jagger',
                     'Julius', 'Lancer', 'Landmark', 'Mace',
                     'Norin61', 'Spelt', 'Stanley', 'Mattis'),
            index=4,
            key='ref')

# Update the index. It is used in the selectbox.
    # st.session_state.index = st.session_state.genome.index(st.session_state.ref)


        refFiles = {'Arina': ['https://www.cerealsdb.uk.net/ibspy_data/aliensArina.csv', '_WhAri'],
                    'Chinese Spring': ['https://www.cerealsdb.uk.net/ibspy_data/aliensChineseSpring.csv', ''],
                    'Jagger': ['https://www.cerealsdb.uk.net/ibspy_data/aliensJagger.csv', '_WhJag'],
                    'Julius': ['https://www.cerealsdb.uk.net/ibspy_data/aliensJulius.csv', '_Whjul'],
                    'Lancer': ['https://www.cerealsdb.uk.net/ibspy_data/aliensLancer.csv', '_Whlan'], 
                    'Landmark': ['https://www.cerealsdb.uk.net/ibspy_data/aliensLandmark.csv', '_WhLan'],
                    'Mace': ['https://www.cerealsdb.uk.net/ibspy_data/aliensMace.csv', '_Whmac'],
                    'Norin61': ['https://www.cerealsdb.uk.net/ibspy_data/aliensNorin61.csv', '_WhNor'],
                    'Spelt': ['https://www.cerealsdb.uk.net/ibspy_data/aliensSpelt.csv', '_Whspe'],
                    'Stanley': ['https://www.cerealsdb.uk.net/ibspy_data/aliensStanley.csv', '_WhSta'],
                    'Mattis': ['https://www.cerealsdb.uk.net/ibspy_data/aliensMattis.csv', '_WhSYM']
                    }

        filePath = refFiles[refGenome][0]

        df = getData(filePath)
        
        df.rename(columns={'timopheevii10558_nuq.jf': 'timopheevii10558_nuq_jf',
                           'timopheevii14352_nuq.jf': 'timopheevii14352_nuq_jf',
                           'timopheevii15832_nuq.jf': 'timopheevii15832_nuq_jf',
                           'timopheevii22438_nuq.jf': 'timopheevii22438_nuq_jf',
                           'timopheevii3708_nuq.jf': 'timopheevii3708_nuq_jf'},
                             inplace=True)

        alienGenomeList = ['Ae. tauschii: BW_01011',
                           'Ae. tauschii: BW_01022',      
                           'Ae. tauschii: BW_01024',      
                           'Ae. tauschii: BW_01026',      
                           'Ae. tauschii: BW_01014',
                           'Ae. tauschii: BW_01028', 
                           'Ae. tauschii: ENT336',
                           'Ae. speltoides: speltoides-10x_nuq',
                           'Ae. ventricosa: ventricosa-10x_nuq',
                           'Ae. ventricosa: ventricosa2067-10x_nuq',     
                           'Ae. ventricosa: ventricosa2181',
                           'Ae. ventricosa: ventricosa2181-10x_nuq',     
                           'Ae. ventricosa: ventricosa2210-10x_all',      
                           'Ae. ventricosa: ventricosa2211-10x_nuq',
                           'Ae. ventricosa: ventricosa2234-10x_all',     
                           'Secale cereale: Lo7_nuq',
                           'Th. elongatum: elongathum-10x_nuq',
                           'Th. ponticum: ponticumG37_nuq',
                           'Th. ponticum: ponticumG38_nuq',     
                           'Th. ponticum: ponticumG39-10x_nuq', 
                           'T. timopheevii: timopheevii3708_nuq.jf',
                           'T. timopheevii: timopheevii10558_nuq.jf',
                           'T. timopheevii: timopheevi10827-10x_nuq',      
                           'T. timopheevii: timopheevii10827-10x-all_all',     
                           'T. timopheevii: timopheevii14352_nuq.jf',     
                           'T. timopheevii: timopheevii15832_nuq.jf',
                           'T. timopheevii: timopheevii17024-10x_all',
                           'T. timopheevii: timopheevii22438_nuq.jf',
                           'T. timopheevii: timopheevi33255-10x_nuq',
                           'T. turgidum ssp. dicoccoides: dicoccoides-10x_nuq',
                           'T. turgidum ssp. durum: svevo-10x_nuq',
                           'T. urartu: urartu-10x_nuq'                      
                           ]
        
        alienGenome1 = st.selectbox(
            'Select first alien species ...',
            alienGenomeList,
            index=29,
            key='alien1'
            )

        alienGenome2 = st.selectbox(
            'Select second alien species ...',
            alienGenomeList,
            index=23,
            key='alien2'
            )         
         
        alien = {'Ae. tauschii: BW_01011': 'BW_01011',
                 'Ae. tauschii: BW_01022': 'BW_01022',      
                 'Ae. tauschii: BW_01024': 'BW_01024',      
                 'Ae. tauschii: BW_01026': 'BW_01026',      
                 'Ae. tauschii: BW_01014': 'BW_01014',
                 'Ae. tauschii: BW_01028': 'BW_01028',        
                 'Ae. tauschii: ENT336': 'ENT336',
                 'Ae. speltoides: speltoides-10x_nuq': 'speltoides-10x_nuq',
                 'Ae. ventricosa: ventricosa-10x_nuq': 'ventricosa-10x_nuq',
                 'Ae. ventricosa: ventricosa2067-10x_nuq': 'ventricosa2067-10x_nuq',   
                 'Ae. ventricosa: ventricosa2181': 'ventricosa2181', 
                 'Ae. ventricosa: ventricosa2181-10x_nuq': 'ventricosa2181-10x_nuq',      
                 'Ae. ventricosa: ventricosa2210-10x_all': 'ventricosa2210-10x_all',      
                 'Ae. ventricosa: ventricosa2211-10x_nuq': 'ventricosa2211-10x_nuq',
                 'Ae. ventricosa: ventricosa2234-10x_all': 'ventricosa2234-10x_all',     
                 'Secale cereale: Lo7_nuq': 'Lo7_nuq',
                 'Th. elongatum: elongathum-10x_nuq': 'elongathum-10x_nuq',
                 'Th. ponticum: ponticumG37_nuq': 'ponticumG37_nuq',
                 'Th. ponticum: ponticumG38_nuq': 'ponticumG38_nuq',     
                 'Th. ponticum: ponticumG39-10x_nuq': 'ponticumG39-10x_nuq',
                 'T. timopheevii: timopheevi33255-10x_nuq': 'timopheevi33255-10x_nuq',
                 'T. timopheevii: timopheevii10558_nuq.jf': 'timopheevii10558_nuq_jf',
                 'T. timopheevii: timopheevi10827-10x_nuq':  'timopheevi10827-10x_nuq',    
                 'T. timopheevii: timopheevii10827-10x-all_all': 'timopheevii10827-10x-all_all',     
                 'T. timopheevii: timopheevii14352_nuq.jf': 'timopheevii14352_nuq_jf',     
                 'T. timopheevii: timopheevii15832_nuq.jf': 'timopheevii15832_nuq_jf',
                 'T. timopheevii: timopheevii17024-10x_all': 'timopheevii17024-10x_all',
                 'T. timopheevii: timopheevii22438_nuq.jf': 'timopheevii22438_nuq_jf',
                 'T. timopheevii: timopheevii3708_nuq.jf': 'timopheevii3708_nuq_jf',     
                 'T. turgidum ssp. dicoccoides: dicoccoides-10x_nuq': 'dicoccoides-10x_nuq',
                 'T. turgidum ssp. durum: svevo-10x_nuq': 'svevo-10x_nuq',
                 'T. urartu: urartu-10x_nuq': 'urartu-10x_nuq'
                 }

        chrm = st.selectbox(
            label='Select chromosome:',
            options=('1A', '2A', '3A', '4A', '5A', '6A', '7A',
                     '1B', '2B', '3B', '4B', '5B', '6B', '7B',
                     '1D', '2D', '3D', '4D', '5D', '6D', '7D'),
            index=8,
            key='chrm')
        
        submit = st.form_submit_button('Submit')


with st.container():
    
    st.markdown('<h1 class="font1">Introgression Viewer</h1>', unsafe_allow_html=True)
    
    st.markdown("""
                       
                ---
                    
                """)
        
    st.markdown("""
                
            To begin exploring potential introgressions, using the dropdown
            menus below, select a reference genome, query genomes (only two
            allowed), and the chromosome you wish to view.

                
            Please note:
                    
            1. Plots and tables can be expanded by clicking on the arrows to their top right.  Hover over the relevant plot or table to see the arrows.
            2. Plots can be downloaded as png or svg format files by clicking on the ellipsis (...) that appears to their top right once you hover over it.
            3. All plots are orientated such that chromosome short arms are on the left.
                
                
            The default plots, below, show the known introgression from *Triticum timopheevii*
            into chromosome 2B of the elite cultivar Lancer (Walkowiak *et al*.
            2020; Keilwagen *et al*., 2022).  This example has been chosen as it
            most clearly illustrates the presence of an introgression.  In the upper
            of the two line plots (*T. timopheevii* hybridised to the reference 
            genome Lancer) the low scores from bin 2,000 to bin 13,000 correspond
            with the known introgression.  By contrast, the plot of *T. dicoccoides* hybridised
            to Lancer shows few or no regions of similarity between the query and the reference genomes.
                
            You may wish to visualise other reported introgressions such as the *Ae. ventricosa*
            introgression on 2AS in the reference genomes Jagger, Mace, SY Mattis and Stanley.


            """)
            
    with st.expander("Cited articles"):
        st.markdown("""
                                                        
                    - 'Walkowiak *et al*. (2020) *Multiple wheat genomes reveal global variation in modern breeding*, **Nature** 588: 277 - 283'
                    - 'Keilwagen *et al*. (2022).  *Detecting major introgressions in wheat and their putative origins using coverage analysis*', **Scientific Reports** 12, 1908
                    - 'Gill, B.S. (2015). *Wheat Chromosome Analysis* In: Ogihara, Y., Takumi, S., Handa, H. (eds) Advances in Wheat Genetics: From Genome to Field. Springer, Tokyo. https://doi.org/10.1007/978-4-431-55675-6_7

                    
                    """
                    )


    st.markdown("""
                
                ---
                
                """
                )

    
col1, col2 = st.columns([3,2], gap='small')

with col1:

    chromosome = 'chr' + chrm + refFiles[refGenome][1]
    # chromosome = 'chr' + st.session_state['chrm'] + refFiles[st.session_state['ref']][1]
    
    dfChr = df[df['seqname'] == chromosome]

    # Adjust the bin number so that it begins at zero (1) for each chromosome.
    dfChr = change_index(dfChr)

    var1 = alien[alienGenome1]
    var2 = alien[alienGenome2]
    

    st.markdown('<p class="font2">Line Plots of Hybridisation Scores</p>', unsafe_allow_html=True)

    chart1_data = dfChr
    a = alt.Chart(chart1_data, title=var1).mark_line(color='#1F77B4').encode(
        x='Adjusted Bin',
        y=var1,
        tooltip=['Adjusted Bin', var1])

    chart1_data = dfChr
    b = alt.Chart(chart1_data, title=var2).mark_line(opacity=0.5, color='#FF7F0E').encode(
        x='Adjusted Bin',
        y=var2,
        tooltip=['Adjusted Bin', var2])

    c = alt.layer(a, b)

    st.altair_chart(c, use_container_width=True)    
   
    with st.expander(f'Chromosome {chrm} diagram'):
        
        chrm_scale = {
            '1A': '1A.png',
            '2A': '2A.png',
            '3A': '3A.png',
            '4A': '4A.png',
            '5A': '5A.png',
            '6A': '6A.png',
            '7A': '7A.png',
            '1B': '1B.png',
            '2B': '2B.png',
            '3B': '3B.png',
            '4B': '4B.png',
            '5B': '5B.png',
            '6B': '6B.png',
            '7B': '7B.png',
            '1D': '1D.png',
            '2D': '2D.png',
            '3D': '3D.png',
            '4D': '4D.png',
            '5D': '5D.png',
            '6D': '6D.png',
            '7D': '7D.png'
            }
        
        st.header(f'Chromosome {chrm}')

        legend1_text = 'Schematic representation of chromosome ' + chrm + ': image length (scale bar) is based on the mean number of 50 Kb bins spanning chromosome ' + chrm + ' in the 11 reference genomes; morphology is based on Gill (2015).  The scale bar is in bin numbers and relates directy to the underlying plots; one can convert length to Mb by multiplying bin number by 50,000.'

        legend1_text_6A = '  Please note, Spelt chromosome '+ chrm + ' is smaller (11,670 bins) than that of the other reference varieties'
        legend1_text_2B = '  Please note, Lancer chromosome ' + chrm + ' is smaller (13,432 bins) than that of the other reference varieties'
        legend1_text_3B = '  Please note, Arina chromosome ' + chrm + ' is larger (17,817 bins) than that of the other reference varieties'
        legend1_text_5B = '  Please note, Arina and SY Mattis carry the chromosome whole arm translocation chromosome 5BS / 7BS rather than 5B.'
        legend1_text_7B = '  Please note, Arina and SY Mattis carry the chromosome whole arm translocation chromosome 5BL / 7BL rather than 7B.'

        if chrm == '6A':
            legend1_text = legend1_text + legend1_text_6A
        elif chrm == '2B':
            legend1_text = legend1_text + legend1_text_2B    
        elif chrm == '3B':
            legend1_text = legend1_text + legend1_text_3B        
        elif chrm == '5B':
            legend1_text = legend1_text + legend1_text_5B 
        elif chrm == '7B':
            legend1_text = legend1_text + legend1_text_7B
        else:
            legend1_text = legend1_text

        st.image('./images/' + chrm_scale[chrm], caption=legend1_text)


with col2:

    st.markdown('<p class="font2">Density Distribution of Scores</p>', unsafe_allow_html=True) 
 
    x1 = dfChr[var1]
    x2 = dfChr[var2]

    # Group data
    hist_data = [x1, x2]

    group_labels = [var1, var2]

    # Create distplot with custom bin_size
    fig = ff.create_distplot(
        hist_data, group_labels)
        
    # Plot the density distribution chart
    st.plotly_chart(fig, use_container_width=True)

dfChr.set_index('Adjusted Bin', inplace=True)
dfChr.drop(columns=['Bin', 'seqname'], inplace=True)
st.write(dfChr)
