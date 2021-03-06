# Autogenerated with SMOP 
from smop.core import *
# 

    
@function
def checkIndex(path=None,file=None,model=None,*args,**kwargs):
    varargin = checkIndex.varargin
    nargin = checkIndex.nargin

    ##
#==============================================================================
# Copyright (c) 2016 Universit de Lorraine & Lule tekniska universitet
# Author: Luca Di Stasio <luca.distasio@gmail.com>
#                        <luca.distasio@ingpec.eu>
    
    # Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 
# Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in
# the documentation and/or other materials provided with the distribution
# Neither the name of the Universit de Lorraine or Lule tekniska universitet
# nor the names of its contributors may be used to endorse or promote products
# derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#==============================================================================
    
    #  DESCRIPTION
#  
#  A function to check if proposed project does not already exist in
#  project's directory. The function reads the .csv file index where for
#  each folder name a string encoding the model is stored. If the input
#  string 'model' encoding the current model parameters is present, exist
#  is set to TRUE, FALSE otherwise.
    
    ##
    
    exist=0
    index=fullfile(path,file)
    fileId=fopen(index)
    C=textscan(fileId,'%s%s','Delimiter',',')
    fclose(fileId)
    for i in arange(1,length(C[2])).reshape(-1):
        oldModel=C[2][i]
        if strcmp(model,oldModel):
            exist=1
            return exist
    
    return exist