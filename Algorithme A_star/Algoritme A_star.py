def algorithme_a_star(start, goal, graph,h):
    #Le chemin qu'on cherche pour aller de start à goal
    chemin=[]
    #les noeuds possibles (clès du graphe)
    pos=[*graph]
    #Ajouter le point de départ à notre chemin
    chemin.append(start)
    #la somme du cout de notre chemin choisit (uniform coast search (g))
    s=0
    for i in range(len(pos)):
        #Commencer par notre  noeud de départ
        if pos[i]==start:
            #les cas possibles pour se déplacer à partir de notre point de départ avec leur cout
            test = graph[pos[i]]
            #trier seulement les noeuds proches du noeud courant
            state=[*test]
            compar={}
            for k in range(len(state)):
                compar[state[k]]=s+test[state[k]]+h[state[k]]
                node=[*compar]
                min=node[0]
                #Si on a plus d'un cas on doit choisir min(f) parmi eux
                if (len(node))>1:
                    for m in range(1,len(node)):
                        if compar[min]> compar[node[m]]:
                            min = node[m]
                #Sinon le seul cas possible pour se dèplacer c'est node[0]
                else:
                    min=node[0]
            #Ajouter à la fin le  noeud suivant à notre chemin
            chemin.append(min)
            #le coût pour atteindre min (g)
            s+=test[min]
            #Sortir de la boucle lorsqu'on a  min==goal , sinon on termine notre chemin en affectant au point de départ le noeud qui le suit(=min)
            if min!=goal:
              start=min
              #En supprimant les noeuds visités dans notre graphe
              del  graph[pos[i]]
              i=0
            else:
                del graph[pos[i]]
                i=len(pos)
    #retourner la liste chemin en chaine en séparant les noeuds par "-"
    result = '-'.join(chemin)
    output = "le chemin optimal est:" + ' ' + result + '  ' + "avec un cout de:" + str(s)
    return (output)