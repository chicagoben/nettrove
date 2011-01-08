#!/usr/bin/env python
#
# Copyright 2011 
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""The Nettrove Communications Library."""

version = "0.1"
version_info = (0, 1, 0)


class nt_endpoint ( object ) :
    def __init__() :
        pass

class nt_inbound ( nt_endpoint ) :
    def __init__() :
        pass

class nt_outbound ( nt_endpoint ) :
    def __init__() :
        pass

class msg_requester ( object ) :
    def __init__() :
        pass

class msg_responder ( object ) :
    def __init__() :
        pass

class msg_publisher ( object ) :
    def __init__() :
        pass

class msg_subscriber ( object ) :
    def __init__() :
        pass

class feed_consumer ( object ) :
    """
    Is both a subscriber and a requester,
    as the user may want to request old or
    missed data in addition to subscribing to
    a live feed.
    """
    def __init__() :
        pass

class feed_producer ( object ) :
    """
    Is both a publisher and a responder,
    as consumers will want to subscribe and
    optionally request missed or old parts 
    of the feed
    """
    def __init__() :
        pass


if __name__ == "__main__" :
    pass

