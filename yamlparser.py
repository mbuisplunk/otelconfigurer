#!/usr/bin/python

import yaml
import PySimpleGUI as psg

with open('agent_config.yaml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    
    #service
    #   extensions
    #   pipelines
    #       traces
    #           receivers
    #           processors
    #           exporters
    #       metrics
    #       metrics/internal
    #       logs/signalfx
    #       logs

    #traces     
    traces_receivers = data['service']['pipelines']['traces']['receivers']
    traces_processors = data['service']['pipelines']['traces']['processors']
    traces_exporters = data['service']['pipelines']['traces']['exporters']

    #metrics
    metrics_receivers = data['service']['pipelines']['metrics']['receivers']
    metrics_processors = data['service']['pipelines']['metrics']['processors']
    metrics_exporters = data['service']['pipelines']['metrics']['exporters']

    #metrics/internal
    metricsinternal_receivers = data['service']['pipelines']['metrics/internal']['receivers']
    metricsinternal_processors = data['service']['pipelines']['metrics/internal']['processors']
    metricsinternal_exporters = data['service']['pipelines']['metrics/internal']['exporters']

    #psg.theme('SandyBeach')
    #define layout
    layout=[[psg.Text('Pipeline Traces Receiver(s)',size=(20, 1), font='Lucida',justification='left')],
            [psg.Listbox(values=['jaeger','otlp','smartagent/signalfx-forwarder', 'zipkin'], select_mode=psg.LISTBOX_SELECT_MODE_MULTIPLE, default_values=traces_receivers,key='tracesReceiverListbox', size=(30, 6))],
            [psg.Text('Pipeline Traces Processor(s)',size=(20, 1), font='Lucida',justification='left')],
            [psg.Listbox(values=['memory_limiter','batch','resourcedetection', 'resource'], select_mode=psg.LISTBOX_SELECT_MODE_MULTIPLE, default_values=traces_processors,key='fac', size=(30, 6))],
            [psg.Text('Pipeline Traces Exporter(s)',size=(20, 1), font='Lucida',justification='left')],
            [psg.Listbox(values=['sapm','otlp','signalfx'], select_mode=psg.LISTBOX_SELECT_MODE_MULTIPLE, default_values=traces_exporters,key='fac', size=(30, 6))],
            
            [psg.Button('SAVE', font=('Times New Roman',12)),psg.Button('CANCEL', font=('Times New Roman',12))]
            
            
            ]
    #Define Window
    win =psg.Window('Splunk Otel Collector Agent Configuration',layout)
    #Read  values entered by user
    e,v=win.read()
    #close first window
    win.close()
    #access the selected value in the list box and add them to a string
    strx=""
    for val in v['tracesReceiverListbox']:
        strx=strx+ " "+ val+","
            
    #display string in a popup         
    psg.popup('Options Chosen',      
                'Selected Values are:' +strx[1:len(strx)-1] )


    # printing the username

    #for receiver in receivers:
    #   print(receiver)

    for traces_receiver in traces_receivers:
        print(traces_receiver)

