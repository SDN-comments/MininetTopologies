'''
@ref: http://mininet.org/walkthrough/#custom-topologies
@author: mk
'''

from mininet.topo import Topo

class Simple3S2H( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )

        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )

        # Add links
        self.addLink( h1, s1 )
        self.addLink( s1, s2 )
        self.addLink( s2, s3 )
        self.addLink( s3, h2 )

topos = { 'mytopo': ( lambda: Simple3S2H() ) }
