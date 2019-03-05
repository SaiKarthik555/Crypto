from parser import Parser
from cube_attack import RandomCubeAttack
from trivium_cube_attack import TriviumCubeAttack

def main():

    args = Parser().args

    if args.mode=="random":

        ca = RandomCubeAttack(degree=args.degree)
        sps = ca.execute_offline_attack()
        equations = ca.execute_online_attack(sps)
        print(ca.possible_maxterms)

    elif args.mode=="trivium":

        f = TriviumCubeAttack(args.n_rounds)

        print(f.test_maxterm("v3v14v21v25v38v43v44v47v54v56v58v68", 675))
        print(f.find_superpoly("v3v14v21v25v38v43v44v47v54v56v58v68"))

main()
