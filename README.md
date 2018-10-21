# RTI Tools

This repository contains a python based RTI driver unpackaging utility. Specifically, it can take an RTI driver and recover the packaged files (javascript code, xml data, etc.).

It is intended to be used for **educational purposes only**.


## RTI Driver Unpackaging
RTI drivers are just OLE files, a container file-type, that contains the RTI driver source files. The different component files (JS code, XML, RTF, etc.) are bundled into streams within the container and then zipped. The unpackaging utility simply removes the streams from the container and unzips them.