import gvar as gv

prior = {}
# not-even leading order 
prior['m_{xi,0}'] = gv.gvar(1000, 1000) # MeV
prior['m_{xi_st,0}'] = gv.gvar(1300, 1000) # MeV
prior['m_{lambda,0}'] = gv.gvar(1000, 1000) 
prior['m_{sigma,0}'] = gv.gvar(1200, 1000) 
prior['m_{sigma_st,0}'] = gv.gvar(1400, 1000)
prior['m_{omega,0}'] = gv.gvar(1650, 1000)
prior['m_{proton,0}'] = gv.gvar(930, 400)
prior['m_{delta,0}'] = gv.gvar(1232,1000)

# lo
prior['s_{xi}'] = gv.gvar(0, 5)
prior['s_{xi,bar}'] = gv.gvar(0, 5)
prior['s_{lambda}'] = gv.gvar(0, 5)
prior['s_{sigma,bar}'] = gv.gvar(0, 5)
prior['s_{sigma}'] = gv.gvar(0, 5)
prior['s_{omega,bar}'] = gv.gvar(0, 5)

# nlo
prior['g_{xi,xi}'] = gv.gvar(0.3, 3)
prior['g_{xi_st,xi}'] = gv.gvar(0.7, 3)
prior['g_{xi_st,xi_st}'] = gv.gvar(-.5, 3)
prior['g_{lambda,sigma}'] = gv.gvar(0, 5)
prior['g_{lambda,sigma_st}'] =gv.gvar(0, 5)
prior['g_{sigma,sigma}'] = gv.gvar(0, 5)
prior['g_{sigma_st,sigma}'] = gv.gvar(0, 5)
prior['g_{sigma_st,sigma_st}']= gv.gvar(0, 5)
prior['g_{proton,delta}'] = gv.gvar(0.91,5)
prior['g_{proton,proton}'] = gv.gvar(1.27,5)
prior['g_{delta,delta}'] = gv.gvar(0.59,5)

# n2lo
prior['a_{xi,4}'] = gv.gvar(0, 5)
prior['a_{xi_st,4}'] = gv.gvar(0, 5)
prior['b_{xi,4}'] = gv.gvar(0, 5)
prior['b_{xi_st,4}'] = gv.gvar(0, 5)
prior['a_{sigma,4}'] = gv.gvar(0, 5)
prior['a_{sigma_st,4}'] = gv.gvar(0, 5)
prior['b_{sigma,4}'] = gv.gvar(0, 5)
prior['b_{sigma_st,4}'] = gv.gvar(0, 5)
prior['a_{lambda,4}'] = gv.gvar(0, 5)
prior['b_{lambda,4}'] = gv.gvar(0, 5)
prior['a_{omega,4}'] = gv.gvar(0, 5)
prior['b_{omega,4}'] = gv.gvar(0, 5)
prior['a_{omega,6}'] = gv.gvar(0, 5)
prior['b_{omega,6}'] = gv.gvar(0, 5)

prior['a_{proton,4}'] = gv.gvar(0, 5)
prior['a_{proton,6}'] = gv.gvar(0, 5)
prior['b_{proton,4}'] = gv.gvar(0,5)
prior['b_{proton,6}'] = gv.gvar(0,5)
prior['b_{proton,2}'] = gv.gvar(0, 5)
prior['g_{delta,4}'] = gv.gvar(0,5)
prior['g_{proton,4}'] = gv.gvar(0,5)
prior['g_{proton,6}'] = gv.gvar(0,5)
prior['d_{proton,a}'] = gv.gvar(0,5)
prior['d_{proton,s}'] = gv.gvar(0,5)
prior['d_{proton,aa}'] = gv.gvar(0,5)
prior['d_{proton,al}'] = gv.gvar(0,5)
prior['d_{proton,as}'] = gv.gvar(0,5)
prior['d_{proton,ls}'] = gv.gvar(0,5)
prior['d_{proton,ss}'] = gv.gvar(0,5)
prior['d_{delta,a}'] = gv.gvar(0,5)
prior['b_{delta,4}'] = gv.gvar(0,5)
prior['a_{delta,4}'] = gv.gvar(0,5)
prior['g_{delta,4}'] = gv.gvar(0,5)
prior['d_{delta,aa}'] = gv.gvar(0,5)
prior['d_{delta,al}'] = gv.gvar(0,5)
prior['d_{delta,as}'] = gv.gvar(0,5)
prior['d_{delta,ls}'] = gv.gvar(0,5)
prior['d_{delta,ss}'] = gv.gvar(0,5)
prior['d_{delta,s}'] = gv.gvar(0,5)
prior['d_{proton,all}'] = gv.gvar(0,5)
prior['d_{proton,aal}'] =  gv.gvar(0,5)


# note: no lo terms for taylor 
# latt/strange nlo
prior['d_{xi,a}'] = gv.gvar(0, 1)
prior['d_{xi_st,a}'] = gv.gvar(0, 1)
prior['d_{xi,s}'] = gv.gvar(0, 1)
prior['d_{xi_st,s}'] = gv.gvar(0, 1)  
prior['d_{lambda,s}'] = gv.gvar(0, 1)
prior['d_{lambda,a}'] = gv.gvar(0, 1)
prior['d_{sigma_st,a}'] = gv.gvar(0, 1) 
prior['d_{sigma_st,s}'] = gv.gvar(0, 1)
prior['d_{sigma,s}'] = gv.gvar(0, 1) 
prior['d_{sigma,a}'] = gv.gvar(0, 1)
prior['d_{omega,s}'] = gv.gvar(0, 1) 
prior['d_{omega,a}'] = gv.gvar(0, 1)
# latt n2lo
prior['d_{xi,aa}'] = gv.gvar(0, 1)
prior['d_{xi,al}'] = gv.gvar(0, 1)
prior['d_{xi,as}'] = gv.gvar(0, 1)
prior['d_{xi,ls}'] = gv.gvar(0, 1)
prior['d_{xi,ss}'] = gv.gvar(0, 1)

prior['d_{xi_st,aa}'] = gv.gvar(0, 1)
prior['d_{xi_st,al}'] = gv.gvar(0, 1) 
prior['d_{xi_st,as}'] = gv.gvar(0, 1)
prior['d_{xi_st,ls}'] = gv.gvar(0, 1) 
prior['d_{xi_st,ss}'] = gv.gvar(0, 1)

prior['d_{lambda,aa}'] = gv.gvar(0, 1)
prior['d_{lambda,al}'] = gv.gvar(0, 1)
prior['d_{lambda,as}'] = gv.gvar(0, 1)
prior['d_{lambda,ls}'] = gv.gvar(0, 1)
prior['d_{lambda,ss}'] = gv.gvar(0, 1)

prior['d_{sigma,aa}'] = gv.gvar(0, 1)
prior['d_{sigma,al}'] = gv.gvar(0, 1)
prior['d_{sigma,as}'] = gv.gvar(0, 1)
prior['d_{sigma,ls}'] = gv.gvar(0, 1)
prior['d_{sigma,ss}'] = gv.gvar(0, 1)

prior['d_{sigma_st,aa}'] = gv.gvar(0, 1)
prior['d_{sigma_st,al}'] = gv.gvar(0, 1) 
prior['d_{sigma_st,as}'] = gv.gvar(0, 1)
prior['d_{sigma_st,ls}'] = gv.gvar(0, 1) 
prior['d_{sigma_st,ss}'] = gv.gvar(0, 1)

prior['d_{omega,aa}'] = gv.gvar(0, 1)
prior['d_{omega,al}'] = gv.gvar(0, 1) 
prior['d_{omega,as}'] = gv.gvar(0, 1)
prior['d_{omega,ls}'] = gv.gvar(0, 1) 
prior['d_{omega,ss}'] = gv.gvar(0, 1)