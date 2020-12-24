#
# Copyright (C) 2020 Lukas Pfeifer
# for cydav version 1.0
#      https://github.com/luv4bytes/cydav
#
# This file is part of cydav.
#
# cydav is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cydav is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with cydav. If not, see <http://www.gnu.org/licenses/>.
#

import subprocess

""" Contains general parameters used by cdav """

class cdav_options:

    # Target URL
    url: str = None

    # User for auth
    user: str = None

    # Password for auth
    password: str = None

    # Don't accept redirects
    no_redirect = False

    # Proxy to use
    proxy: str = None

    # Show raw output
    raw = False

    # Cdav file to use
    cdav_file: str = None

    # Print help
    help = False

    # Print version
    version = False


""" Control class for cdav """

class cdav:

    cdav_path = None

    def __init__(self, cdav_path: str):
        self.cdav_path = cdav_path

    def __create_args(self, options: cdav_options) -> []:
        args = []

        args.append(self.cdav_path)

        if options.url:
            args.append("-a")
            args.append(options.url)

        if options.user:
            args.append("-u")
            args.append(options.user)

        if options.password:
            args.append("-pw")
            args.append(options.password)

        if options.no_redirect == True:
            args.append("--no-redirect")

        if options.proxy:
            args.append("--proxy")
            args.append(options.proxy)

        if options.raw == True:
            args.append("--raw")

        if options.cdav_file:
            args.append("-f")
            args.append(options.cdav_file)

        if options.help == True:
            args.append("-h")

        if options.version == True:
            args.append("-v")

        return args

    """ Start cdav with operation GET """

    def GET(self, options: cdav_options, save_as: str):

        try:
            args = self.__create_args(options)

            args.append("-o")
            args.append("GET")

            if save_as:
                args.append("-s")
                args.append(save_as)

            result = subprocess.check_output(args)

        except Exception as ex:
            return ex

        return result

    """ Start cdav with operation PUT """

    def PUT(self, options: cdav_options, upload_file: str):

        try:
            args = self.__create_args(options)

            args.append("-o")
            args.append("PUT")

            if upload_file:
                args.append("-uf")
                args.append(upload_file)

            result = subprocess.check_output(args)

        except Exception as ex:
            return ex

        return result

    """ Start cdav with operation PROPFIND """

    def PROPFIND(self, options: cdav_options, props: str, depth):

        try:
            args = self.__create_args(options)

            args.append("-o")
            args.append("PROPFIND")

            if props:
                args.append("-p")
                args.append(props)

            if depth:
                args.append("-d")
                args.append(depth)

            result = subprocess.check_output(args)

        except Exception as ex:
            return ex

        return result

    """ Start cdav with operation PROPPATCH """

    def PROPPATCH(self, options: cdav_options, set_props: str, rm_props: str):

        try:
            args = self.__create_args(options)

            args.append("-o")
            args.append("PROPPATCH")

            if set_props:
                args.append("-sp")
                args.append(set_props)

            if rm_props:
                args.append("-rp")
                args.append(rm_props)

            result = subprocess.check_output(args)

        except Exception as ex:
            return ex

        return result

    """ Start cdav with operation COPY """

    def COPY(self, options: cdav_options, destination: str, no_overwrite: bool):

        try:
            args = self.__create_args(options)

            args.append("-o")
            args.append("COPY")

            if destination:
                args.append("-da")
                args.append(destination)

            if no_overwrite == True:
                args.append("--no-overwrite")

            result = subprocess.check_output(args)

        except Exception as ex:
            return ex

        return result

    """ Start cdav with operation MOVE """

    def MOVE(self, options: cdav_options, destination: str, no_overwrite: bool):

        try:

            args = self.__create_args(options)

            args.append("-o")
            args.append("MOVE")

            if destination:
                args.append("-da")
                args.append(destination)

            if no_overwrite == True:
                args.append("--no-overwrite")

            result = subprocess.check_output(args)

        except Exception as ex:
            return ex

        return result

    """ Start cdav with operation LOCK """

    def LOCK(self, options: cdav_options, lock_scope: str, lock_owner: str, depth):

        try:

            args = self.__create_args(options)

            args.append("-o")
            args.append("LOCK")

            if lock_scope:
                args.append("-ls")
                args.append(lock_scope)

            if lock_owner:
                args.append("-lo")
                args.append(lock_owner)

            if depth:
                args.append("-d")
                args.append(depth)

            result = subprocess.check_output(args)

        except Exception as ex:
            return ex

        return result

    """ Start cdav with operation UNLOCK """

    def UNLOCK(self, options: cdav_options, lock_token: str):

        try:

            args = self.__create_args(options)
            
            args.append("-o")
            args.append("UNLOCK")

            if lock_token:
                args.append("-lt")
                args.append(lock_token)

            result = subprocess.check_output(args)

        except Exception as ex:
            return ex

        return result